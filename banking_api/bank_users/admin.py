from django.contrib import admin
from .models import Users, UserBeneficiaries
# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["user_id","username", "password", "fullname", "email", "user_status"]
    list_editable = ["username", "password", "fullname", "email", "user_status"]
    list_filter = ["user_status"]


@admin.register(UserBeneficiaries)
class UserBeneficiariesAdmin(admin.ModelAdmin):
    list_display = ["id", "user_id", "beneficiary_fullname", "beneficiary_account_no", "other_bank_id", "is_guest"]
    ordering = ["user_id", "is_guest"]