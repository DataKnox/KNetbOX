import requests
import json

base_url = "http://localhost:8000/api"

headers = {
    'accept': 'application/json',
    'Authorization': 'Token 0123456789abcdef0123456789abcdef01234567',

}


def get_dev_roles():
    dev_roles_url = "/dcim/device-roles/"
    print(headers)
    try:
        dev_roles = requests.get(
            url=f"{base_url}{dev_roles_url}", headers=headers, verify=False)
        if dev_roles.status_code == 200:
            return json.loads(dev_roles.text)['results']
    except Exception as err:
        return err


def get_dev_types():
    dev_types_url = "/dcim/device-types/"
    try:
        dev_types = requests.get(
            url=f"{base_url}{dev_types_url}", headers=headers, verify=False)
        if dev_types.status_code == 200:
            return json.loads(dev_types.text)['results']
    except Exception as err:
        return err


def get_manufacturers():
    manu_url = '/dcim/manufacturers/'
    try:
        manus = requests.get(
            url=f"{base_url}{manu_url}", headers=headers, verify=False)
        if manus.status_code == 200:
            return json.loads(manus.text)['results']
    except Exception as err:
        return err


def get_sites():
    sites_url = '/dcim/sites/'
    try:
        sites = requests.get(
            url=f"{base_url}{sites_url}", headers=headers, verify=False)
        if sites.status_code == 200:
            return json.loads(sites.text)['results']
    except Exception as err:
        return err


def get_devices():
    devices_url = '/dcim/devices/'
    try:
        devices = requests.get(
            url=f"{base_url}{devices_url}", headers=headers, verify=False)
        if devices.status_code == 200:
            return json.loads(devices.text)['results']
    except Exception as err:
        return err


def get_tenants():
    tenant_url = '/tenancy/tenants/'
    try:
        tenants = requests.get(
            url=f"{base_url}{tenant_url}", headers=headers, verify=False)
        if tenants.status_code == 200:
            return json.loads(tenants.text)['results']
    except Exception as err:
        return err


if __name__ == "__main__":
    # print(json.dumps(get_dev_roles(), indent=2))
    # print(json.dumps(get_dev_types(), indent=2))
    # print(json.dumps(get_manufacturers(), indent=2))
    # print(json.dumps(get_sites(), indent=2))
    # print(json.dumps(get_devices(), indent=2))
    print(json.dumps(get_tenants(), indent=2))
