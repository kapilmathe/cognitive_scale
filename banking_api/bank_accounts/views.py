import logging
from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .models import BankBranch, BankAccounts, BankAccountSerializer
from bank_users.models import Users


logger = logging.getLogger(__name__)
# Create your views here.
@api_view(['POST'])
def create_bank_account(request):
    out = {'success': True, 'account_number': None}

    branch_code = request.data.get('branch_code')
    client_id = request.data.get('client_id')
    initial_amount = request.data.get('initial_amount')

    try:
        branch = BankBranch.objects.get(branch_code = branch_code)
        client = Users.objects.get(user_id = client_id)
        if branch:
            account = branch.create_bank_account(
                client_id=client,
                initial_amount=initial_amount
            )

            if account:
                out['account_number'] = account.account_no
                return Response(out, status.HTTP_201_CREATED)
            else:
                out['success'] = False
                return Response(out, status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        logger.error("failed to create account: {0}".format(err))
        out['success'] = False
        return Response(out, status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['GET'])
def get_bank_accounts(request):
    out = {'success': True, 'data': None}
    try:
        accounts = BankAccounts.objects.all().prefetch_related('bank_branch')
        data = BankAccountSerializer(accounts, many=True)
        if data.data:
            out['data'] = data.data
            return Response(out, status.HTTP_200_OK)
        else:
            return Response(out, status.HTTP_204_NO_CONTENT)
    except Exception as err:
        logger.error("failed to fetch bank accounts: {0}".format(err))
        out['success'] = False
        return Response(out, status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['GET'])
def get_balance(request, account_no):
    out = {'success': True, 'data': None}
    account_no = account_no # request.data.get('account_no')
    try:
        account = BankAccounts.objects.get(account_no=account_no)
        out['data'] = {'balance': account.get_balance()}
        return Response(out, status.HTTP_200_OK)
    except Exception as err:
        logger.error("failed to get balance:{0]".format(err))
        out['success'] = False
        return Response(out, status.HTTP_503_SERVICE_UNAVAILABLE)
