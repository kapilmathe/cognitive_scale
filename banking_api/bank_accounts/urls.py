from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_account/$', views.create_bank_account),
    url(r'^get_bank_accounts/$', views.get_bank_accounts),
    url(r'^get_balance/(\d+)/$', views.get_balance)
]