"""banking_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from bank_users import urls as bank_user_urls
from bank_accounts import urls as bank_accounts_urls
from bank_transactions import urls as bank_transactions_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bank_users/', include(bank_user_urls)),
    url(r'^bank_accounts/', include(bank_accounts_urls)),
    url(r'^bank_transactions/', include(bank_transactions_urls))

]
