from django.db import models

# Create your models here.
class TransactionsDeposit(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    account_no = models.CharField(max_length=13)
    transaction_info = models.CharField(max_length=1024)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def move_to_history(self):
        tx_history = TransactionsDepositHistory(
            transaction_id= self.transaction_id,
            account_no = self.account_no,
            transaction_info = self.transaction_info,
            amount = self.amount,
            created_on = self.created_on,
            status = self.status
        )
        tx_history.save()


class TransactionsWithdraw(models.Model):
    transaction_id = models.BigAutoField(primary_key=True)
    account_no = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    transaction_info = models.CharField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

    def move_to_history(self):
        tx_history = TransactionsWithdrawHistory(
            transaction_id= self.transaction_id,
            account_no = self.account_no,
            transaction_info = self.transaction_info,
            amount = self.amount,
            created_on = self.created_on,
            status = self.status
        )
        tx_history.save()


class TransactionsDepositHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    transaction_id = models.BigIntegerField()
    account_no = models.CharField(max_length=13)
    transaction_info = models.CharField(max_length=1024)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)

class TransactionsWithdrawHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    transaction_id = models.BigIntegerField()
    account_no = models.CharField(max_length=13)
    amount = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    transaction_info = models.CharField(max_length=1024)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    status = models.BooleanField(default=True)


class ScheduleTransactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    schedule_date = models.DateTimeField()
    transaction_order_list = models.TextField(max_length=2048)
    status = models.SmallIntegerField()
