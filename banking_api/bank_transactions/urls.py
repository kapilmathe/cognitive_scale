from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^deposit/$', views.deposit),
    url(r'^withdraw/$', views.withdraw),
    url(r'^schedule/$', views.schedule),
    url(r'^fund_transfer/$', views.fund_transfer),
    url(r'^transaction_summary/$', views.transaction_summary),
]