from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_account/$', views.create_bank_account),
    url(r'^delete_account/$', views.delete_bank_account),
    url(r'^get_bank_accounts/$', views.get_bank_accounts),
    url(r'^get_balance/(\d+)/$', views.get_balance),
    url(r'^get_future_balance/(\d+)/$', views.future_balance),
    url(r'^get_other_bank_branch/(\w+)$', views.get_other_bank_branch),


]