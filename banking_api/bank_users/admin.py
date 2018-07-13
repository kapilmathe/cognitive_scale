from django.contrib import admin
from .models import Users
# Register your models here.
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["user_id","username", "password", "fullname", "email", "user_status"]
    list_editable = ["username", "password", "fullname", "email", "user_status"]
    list_filter = ["user_status"]