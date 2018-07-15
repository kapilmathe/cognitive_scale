import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Users, UserSerializer, UserBeneficiaries
from passlib.hash import pbkdf2_sha256
from bank_accounts.models import OtherBanks, BankAccounts


logger = logging.getLogger(__name__)
# Create your views here.
@api_view(['POST'])
def create_user(request):
    out = {'success': True, 'user_id': None}
    if request.data:
        username = request.data.get('username')
        fullname = request.data.get('fullname')
        password = request.data.get('password')
        email = request.data.get('email')
        user_status = request.data.get('user_status', False)
        try:
            encrypted_pwd = pbkdf2_sha256.encrypt(password)
            user = Users(
                username=username,
                fullname=fullname,
                password=encrypted_pwd,
                email=email,
                user_status =user_status,
            )
            user.save()
            out['user_id'] = user.user_id
            return Response(out, status.HTTP_201_CREATED)
        except Exception as err:
            logger.error("failed to create user: {0]".format(err))
            out['success'] = False
            return Response(out, status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_list(request):
    out = {'success': True  ,'data': None}
    users = Users.objects.all()
    print(users)
    data = UserSerializer(users,many=True)
    data = data.data
    print(data)
    # data  =  serializers.serialize(queryset=users, format='json')
    out['data'] = data
    return Response(out, status.HTTP_200_OK)


@api_view(['POST'])
def add_beneficiary(request):
    out = {'success': True, 'data': None}

    username = request.data.get('username')
    beneficiary_name = request.data.get('beneficiary_name')
    beneficiary_account_no = request.data.get('beneficiary_account_no')
    beneficiary_nickname = request.data.get('beneficiary_nickname')
    bank_branch_code = request.data.get('branch_code')

    # other bank account
    try:
        user = Users.objects.get(username=username)
        if bank_branch_code:
            # other_bank = req.get('http://localhost:8000/get_other_bank_branch/{0}'.format(bank_branh_code))
            # if other_bank.status_code == 200:
            #     other_bank_info = json.loads(other_bank.text)
            # else:
            #     return Response(out, status.HTTP_400_BAD_REQUEST)
            other_bank = OtherBanks.objects.filter(bank_branch_code=bank_branch_code).first()
            other_bank_user = None
            if other_bank:
                beneficiary = UserBeneficiaries(
                    user_id=user,
                    nickname=beneficiary_nickname,
                    beneficiary_account_no= beneficiary_account_no,
                    beneficiary_fullname=beneficiary_name,
                    other_bank_id=other_bank,
                    is_guest=True
                )
                beneficiary.save()
                return Response(out, status.HTTP_201_CREATED)
            else:
                out['success']=False
                return Response(out, status.HTTP_400_BAD_REQUEST)
        else:
            existing_local_account = BankAccounts.objects.filter(account_no=beneficiary_account_no ).first()
            if existing_local_account:
                if beneficiary_name == existing_local_account.client_id.fullname:
                    beneficiary = UserBeneficiaries(
                        user_id=user,
                        nickname=beneficiary_nickname,
                        beneficiary_account_no=beneficiary_account_no,
                        beneficiary_fullname=beneficiary_name,
                        is_guest=False
                    )
                    beneficiary.save()
                    return Response(out, status.HTTP_201_CREATED)
                else:
                    out['success'] = False
                    out['error'] = "not bank account beneficiary"
                    return Response(out, status.HTTP_400_BAD_REQUEST)
            else:
                out['success']=False
                return Response(out, status.HTTP_400_BAD_REQUEST)

    except Exception as err:
        logger.error("failed to add beneficiary:{0}".format(err))
        out['success']=False
        return Response(out, status.HTTP_503_SERVICE_UNAVAILABLE)


@api_view(['POST'])
def delete_beneficiary(request):
    out = {'success': True}
    id =request.data.get('beneficiary_id')
    try:
        if id:
            UserBeneficiaries.objects.filter(id=id).delete()
            return Response(out, status.HTTP_202_ACCEPTED)
        else:
            out['success'] = False
            return Response(out, status.HTTP_400_BAD_REQUEST)
    except Exception as err:
        logger.error("failed to delete beneficiary:{0}".format(err))
        out['success'] = False
        return Response(out, status.HTTP_503_SERVICE_UNAVAILABLE)
