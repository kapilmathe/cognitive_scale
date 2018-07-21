from django.test import TestCase
import json
from banking_api.settings import HOST
import requests
# Create your tests here.


def test_get_bank_accounts():
    url = "{0}/bank_accounts/get_bank_accounts/".format(HOST)
    res = requests.get(url)
    if res.status_code:
        if res.status_code == 200:
            return res.status_code
    raise Exception("get bank accounts api call failed with error_code:{0}".format(res.status_code))



def test_get_balance():
    url = "{0}/bank_accounts/get_balance/3".format(HOST)
    res = requests.get(url)
    if res.status_code:
        if res.status_code == 200:
            return res.status_code
    raise Exception("get_balance api call failed with error_code:{0}".format(res.status_code))



def test_future_balance():
    url = "{0}/bank_accounts/get_future_balance/3".format(HOST)
    res = requests.get(url)
    if res.status_code:
        if res.status_code == 200:
            return res.status_code
    raise Exception("get_future_balance api call failed with error_code:{0}".format(res.status_code))



def test_get_other_bank_branch():
    url = "{0}/bank_accounts/get_other_bank_branch/CITI00001".format(HOST)
    res = requests.get(url)
    if res.status_code:
        if res.status_code == 200:
            return res.status_code
    raise Exception("get_other_bank_branch api call failed with error_code:{0}".format(res.status_code))



def test_create_account():
    url = "{0}/bank_accounts/create_account/".format(HOST)
    req_params = {
        'branch_code': 'ICICI00031',
        'client_id': 5,
        'initial_amount': 6000
    }
    res = requests.post(url, req_params)
    if res.status_code:
        if res.status_code == 201:
            respnse = json.loads(res.text)
            account_no = respnse.get("account_number")
            delete_url = "{0}/bank_accounts/delete_account/".format(HOST)
            del_res = requests.post(delete_url, {"account_no": account_no})
            if del_res.status_code == 202:
                return res.status_code
            else:
                raise Exception("reverting test case changes failed")
    raise Exception("create bank accounts api call failed with error_code:{0}".format(res.status_code))
