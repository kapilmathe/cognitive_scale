from django.db import models

# Create your models here.
class Transactions(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    depositor_account_no = models.CharField(max_length=13)
    recipient_account_no = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)


class TransactionsSucceeded(models.Model):
    transaction_histid = models.BigAutoField(primary_key=True)
    transaction_id = models.BigIntegerField()
    depositor_account_no = models.CharField(max_length=13)
    recipient_account_no = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

class TransactionsFailed(models.Model):
    transaction_histid = models.BigAutoField(primary_key=True)
    transaction_id = models.BigIntegerField()
    depositor_account_no = models.CharField(max_length=13)
    recipient_account_no = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)