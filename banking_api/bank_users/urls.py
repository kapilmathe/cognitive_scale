from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_user/', views.create_user),
    url(r'^delete_user/', views.delete_user),
    url(r'^get_users/', views.get_user_list),
    url(r'^add_beneficiary/$', views.add_beneficiary),
    url(r'^delete_beneficiary/$', views.delete_beneficiary),
]