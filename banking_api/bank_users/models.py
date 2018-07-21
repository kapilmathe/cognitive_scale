from django.db import models
from rest_framework import  serializers
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

    def __str__(self):
        return "{0}-{1}".format(self.username, self.fullname)


    class Meta:
        verbose_name_plural = "Users"


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=256)
    fullname = serializers.CharField(max_length=256)
    email = serializers.CharField(max_length=256)
    user_status = serializers.BooleanField()


# this model can be moved to bank_accounts module.
class UserBeneficiaries(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10)
    beneficiary_account_no = models.CharField(max_length=13, db_index=True)
    beneficiary_fullname = models.CharField(max_length=256)
    other_bank_id = models.ForeignKey('bank_accounts.OtherBanks', on_delete=models.CASCADE, null=True)
    is_guest = models.BooleanField()

    class Meta:
        verbose_name_plural = "User Beneficiaries"


class UserBeneficiariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBeneficiaries
        fields = '__all__'
        depth = 1