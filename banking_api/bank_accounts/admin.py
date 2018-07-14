from django.contrib import admin
from .models import BankBranch, OtherBanks, BankAccounts

# Register your models here.
@admin.register(BankBranch)
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ["branch_id", "branch_code", "branch_name", "branch_address"]
    list_editable = ["branch_code", "branch_name", "branch_address"]


@admin.register(OtherBanks)
class OtherBanksAdmin(admin.ModelAdmin):
    list_display = ["bank_id","bank_name", "bank_branch_code", "bank_branch_info"]
    list_editable = ["bank_name", "bank_branch_code", "bank_branch_info"]


@admin.register(BankAccounts)
class BankAccountsAdmin(admin.ModelAdmin):
    list_display = ["account_id", "account_no", "bank_branch", "amount", "client_id"]