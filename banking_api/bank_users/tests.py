from django.test import TestCase
import json
from banking_api.settings import HOST
import requests

# Create your tests here.

def test_create_user():
    req_params = {
    'username' :'test02',
    'fullname': 'Test 02',
    'password': '',
    'email': 'test02@gmail.com',
    'user_status': False
    }
    url = "{0}/bank_users/create_user/".format(HOST)
    res = requests.post(url, req_params)
    if res.text:
        respnse = json.loads(res.text)
        if respnse.get('success'):
            if respnse.get('user_id'):
                user_id = respnse.get('user_id')
                delete_url = url = "{0}/bank_users/delete_user/".format(HOST)
                del_res = requests.post(url, {'user_id': user_id})
                if del_res.status_code == 202:
                    return res.status_code
                else:
                    Exception("reverting test changes failed:delete_user api call failed with error_code:{1}: {0}".format(del_res.text, del_res.status_code))
    raise Exception("create user api call failed with error_code:{1}: {0}".format(res.text, res.status_code))


def test_get_users():
    url = "{0}/bank_users/get_users/".format(HOST)
    res = requests.get(url)
    if res.status_code:
        if res.status_code == 200:
            return res.status_code
    raise Exception("get user api call failed with error_code:{0}".format(res.status_code))


def test_add_beneficiary():
    url = "{0}/bank_users/add_beneficiary/".format(HOST)
    req_params = {
        'username': 'zonda',
        'beneficiary_name': 'Kamlesh Mathe',
        'beneficiary_account_no': 3,
        'beneficiary_nickname': 'kammu_zonda'
    }
    res = requests.post(url, req_params)
    if res.text:
        response = json.loads(res.text)
        if response.get('success'):
            if res.status_code == 201:
                return res.status_code
    raise Exception("add beneficiary api call failed with error_code:{1}: {0}".format(res.text, res.status_code))


def test_delete_beneficiary():
    url = "{0}/bank_users/delete_beneficiary/".format(HOST)
    req_params = {
        'beneficiary_id':11
    }
    res = requests.post(url, req_params)
    if res.status_code == 202:
        return res.status_code
    raise Exception("delete beneficiary api call failed with error_code:{1}: {0}".format(res.text, res.status_code))