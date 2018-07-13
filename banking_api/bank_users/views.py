import logging
from django.shortcuts import render
from django.core import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from .models import Users, UserSerializer
from passlib.hash import pbkdf2_sha256


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