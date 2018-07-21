from django.test import TestCase
import json
from banking_api.settings import HOST
import requests

# Create your tests here.
def test_fund_transfer():
    req_params = {
        'beneficiary_account_no' : 12,
        'amount': 5000,
        'account_no': 2,
        'transaction_info:': 'test transfer',
    }
    url = "{0}/bank_transactions/fund_transfer/".format(HOST)
    res = requests.post(url, req_params)
    if res.status_code == 201:
        return res.status_code
    raise Exception("fund transfer api call failed with error_code:{1}: {0}".format(res.text, res.status_code))