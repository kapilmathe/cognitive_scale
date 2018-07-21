import logging
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from bank_accounts.models import BankAccounts
from decimal import Decimal
import requests
import json


logger = logging.getLogger(__name__)
# Create your views here.
@api_view(['POST'])
@transaction.atomic
def deposit(request):

    out = {'success': True, 'message': None}
    beneficiary_account_no = request.data.get('beneficiary_account_no')
    amount = request.data.get('amount')
    schedule = request.data.get('schedule')
    transaction_type = request.data.get('transaction_type')

    transaction_info = request.data.get('transaction_info')
    tx = TransactionsDeposit(account_no=beneficiary_account_no,
                                      transaction_info=transaction_info,
                                      amount=amount,
                                      status=False)
    tx.save()

    try:
        if schedule and transaction_type:
            sch = ScheduleTransactions(schedule_date=schedule,
                                       transaction_order_list= "{0}".format(tx.transaction_id),
                                       status=0,)
            sch.save()
            out['message'] = "deposit scheduled for {0}".format(schedule)
            return Response(out, status.HTTP_201_CREATED)
        elif schedule:
            out['message'] = tx.transaction_id
            return Response(out, status.HTTP_201_CREATED)

        with transaction.atomic():
            bank_account = BankAccounts.objects.get(account_no = beneficiary_account_no)
            bank_account.add_amount(amount)
            tx.status = True
            bank_account.save()
            out['message'] = "amount: {0} deposited successfully".format(amount)

        tx.save()
        tx.move_to_history()
        tx.delete()

        return Response(out, status.HTTP_201_CREATED)
    except Exception as err:
        out['success'] = False
        logger.error("failed to deposit:{0}".format(err))
        # out['message'] = err
        tx.move_to_history()
        tx.delete()
        return Response(out, status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
@transaction.atomic
def withdraw(request):
    out = {'success': True, 'message': None,}
    beneficiary_account_no = request.data.get('beneficiary_account_no')
    amount = request.data.get('amount')
    transaction_info = request.data.get('transaction_info')
    schedule = request.data.get('schedule')
    transaction_type = request.data.get('transaction_type')

    tx = TransactionsWithdraw(account_no=beneficiary_account_no,
                                      transaction_info=transaction_info,
                                      amount=amount,
                                      status=False)
    tx.save()
    try:
        if schedule and transaction_type:
            sch = ScheduleTransactions(schedule_date=schedule,
                                       transaction_order_list= "{0}".format(tx.transaction_id),
                                       status=0,)
            sch.save()
            out['message'] = "Withdraw scheduled for {0}".format(schedule)
            return Response(out, status.HTTP_201_CREATED)
        elif schedule:
            out['message'] = tx.transaction_id
            return Response(out, status.HTTP_201_CREATED)

        with transaction.atomic():
            bank_account = BankAccounts.objects.get(account_no=beneficiary_account_no)
            balance = bank_account.get_balance()
            if balance < Decimal(amount):
                out['message'] = "Insufficient Balance"
                raise Exception(out['message'])
            else:
                if bank_account.reduce_amount(amount):
                    bank_account.save()
                    tx.status = True
                    tx.save()
        out['message'] = "amount: {0} withdraw successfully".format(amount)
        tx.move_to_history()
        tx.delete()
        return Response(out, status.HTTP_201_CREATED)
    except Exception as err:
        out['success'] = False
        logger.error("failed to withdraw:{0}".format(err))
        # out['message'] = err
        tx.move_to_history()
        tx.delete()
        return Response(out, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@transaction.atomic
def fund_transfer(request):
    out = {'success': True, 'message': None}

    account_no = request.data.get('account_no')
    beneficiary_account_no = request.data.get('beneficiary_account_no')
    amount = request.data.get('amount')
    transaction_info = request.data.get('transaction_info')
    schedule = request.data.get('schedule')

    try:

        withdraw = requests.post(
            url = 'http://localhost:8000/bank_transactions/withdraw/',
            data={'beneficiary_account_no': account_no,
                  'amount': amount,
                  'transaction_info': "Transferring to {0}/{1}".format(beneficiary_account_no,transaction_info),
                  'schedule': schedule,
                  }
        )
        logger.info(withdraw.text, withdraw.status_code)
        # print(withdraw.text, withdraw.status_code)
        if withdraw.status_code == 201:
            deposit = requests.post(
                url = 'http://localhost:8000/bank_transactions/deposit/',
                data={'beneficiary_account_no': beneficiary_account_no,
                      'amount': amount,
                      'transaction_info': "Amount received from  to {0}/{1}".format(account_no,transaction_info),
                      'schedule': schedule,
                      },
            )
            logger.info(deposit.text, deposit.status_code)
            # print(deposit.text, deposit.status_code)
            if deposit.status_code == 201:
                out['message'] = "fund transfferred successfully"
                return Response(out, status.HTTP_201_CREATED)
            else:
                revert = 400
                no_of_retry = 3
                while revert != 201 and no_of_retry > 0:
                    revert_req = requests.post(
                        url='http://localhost:8000/bank_transactions/deposit/',
                        data={'beneficiary_account_no': account_no,
                              'amount': amount,
                              'transaction_info': "Reverting amount {0}".format(transaction_info)
                              },
                    )
                    revert = revert_req.status_code
                    no_of_retry -= 1
                raise Exception("Transfer failed")
        else:
            out['success'] = False
            out['message'] = json.loads(withdraw.text)
            return Response(out, status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        out['success'] = False
        out['message'] = "Failed to Transfer fund"
        logger.error("failed to withdraw:{0}".format(err))
        return Response(out, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def transaction_summary(request):
    pass


@api_view(['POST'])
def schedule(request):
    out = {'success': True, 'message': None}
    try:
        return Response(out, status.HTTP_201_CREATED)
    except Exception as err:
        logger.error("failed to schedule:{0}".format(err))
        return Response(out, status.HTTP_400_BAD_REQUEST)
