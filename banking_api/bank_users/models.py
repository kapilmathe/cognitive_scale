from django.db import models
from django.apps import apps
# OtherBanks = apps.get_model('bank_accounts', 'OtherBanks')
# from bank_accounts.models import *
from passlib.hash import pbkdf2_sha256
# Create your models here.

class Users(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=256, unique=True, db_index=True)
    password = models.CharField(max_length=256)
    fullname = models.CharField(max_length=256)
    email = models.EmailField(max_length=256, default="abc@gmail.com")
    user_status = models.BooleanField(default=False)

    def verify_password(self, raw_password):
        return pbkdf2_sha256.verify(raw_password, self.password)

    def set_user_status(self, status):
        self.user_status = status

    class Meta:
        verbose_name_plural = "Users"

class OtherBankUserInfo(models.Model):
    guest_user_id = models.BigAutoField(primary_key=True)
    guest_fullname = models.CharField(max_length=256)
    other_bank_id = models.ForeignKey('bank_accounts.OtherBanks', on_delete=models.CASCADE)
    other_bank_account_no = models.CharField(max_length=13, unique=True, db_index=True)


class UserBeneficiaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    beneficiary_id= models.BigIntegerField()
    nickname = models.CharField(max_length=10)
    beneficiary_account_no = models.CharField(max_length=13, unique=True, db_index=True)
    beneficiary_fullname = models.CharField(max_length=256)
    is_guest = models.BooleanField()


