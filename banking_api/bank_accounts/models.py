from django.db import models
from django.apps import apps
# Users = apps.get_model('bank_users', 'Users')
# from bank_users.models import *
# from banking_api.bank_users.models import Users

# Create your models here.
class BankBranch(models.Model):
    branch_id = models.BigAutoField(primary_key=True)
    branch_code = models.CharField(max_length=10, unique=True, db_index=True)
    branch_name = models.CharField(max_length=100)
    branch_address = models.CharField(max_length=1024, null=True)

    def get_available_account_no(self):
        available_account_no = AccontNumberGenerator(is_valid = True)
        available_account_no.save()
        return available_account_no.id

    def create_bank_account(self, client_id, initial_amount= 0):
        account_no = self.get_available_account_no()
        account = BankAccounts(
            account_no= account_no,
            bank_branch = self,
            amount= initial_amount,
            client_id=client_id
        )
        try:
            account.save()
            return account.account_no
        except Exception as err:
            print("failed to create account: {0}".format(err))
            return -1

    class Meta:
        verbose_name_plural = "BankBranch"


class OtherBanks(models.Model):
    bank_id = models.BigAutoField(primary_key=True)
    bank_name = models.CharField(max_length=100)
    bank_branch_code = models.CharField(max_length=10, unique=True, db_index=True)
    bank_branch_info = models.CharField(max_length=1024, null=True)

    class Meta:
        verbose_name_plural = "OtherBanks"


class BankAccounts(models.Model):
    account_id = models.BigAutoField(primary_key=True)
    account_no = models.CharField(max_length=13, unique=True, db_index=True)
    bank_branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    client_id = models.ForeignKey('bank_users.Users', on_delete=models.CASCADE)

    def get_balance(self):
        return self.amount

class AccontNumberGenerator(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_valid = models.BooleanField(default=True)
