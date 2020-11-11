import pynetbox
from collector import get_inv_details
from configer import config_gen
from nornir import InitNornir
from nornir_scrapli.tasks import (
    get_prompt,
    send_command,
    send_commands,
    send_configs
)
from nornir_utils.plugins.functions import print_result
from nornir.core.task import Task, Result
import logging
from nornir_scrapli.functions import print_structured_result
from knetbox_getter import (
    get_dev_roles, get_dev_types, get_devices, get_manufacturers, get_sites, get_tenants)


nb = pynetbox.api(
    'http://10.10.21.196:8000',
    token='0123456789abcdef0123456789abcdef01234567')


def device_creator(task):
    # Check if device already exists
    device = task.run(task=get_inv_details)
    hostname = device['hostname']
    serial = device['serial']
    existing_devices = get_devices()
    for ex_device in existing_devices:
        if ex_device == device['hostname']:
            return "Device already exists in inventory"

    # Handle site ID
    print(nb.dcim.sites.all())
    site = input("Choose a site from above list: ")
    existing_sites = get_sites()
    for ex_site in existing_sites:
        if ex_site['name'] == site:
            site_id = ex_site['id']
        else:
            print("Something went wrong with getting Site")

    # Handle Role ID
    existing_roles = get_dev_roles()
    role = 'Virtual'
    for int in device['interfaces']:
        if int['media'] != 'Virtual':
            role = int['media']
        else:
            print('Virtual device detected')
            role = input('Choose one: ["virtual router", "virtual switch"]')
    if role == 'Virtual':
        tenants = get_tenants()
        for tenant in tenants:
            if tenant['name'] == role:
                ten_id = tenant['id']
    for ex_role in existing_roles:
        if ex_role['name'] == role:
            role_id = ex_role['id']
        else:
            print("Something went wrong with getting Role ID")

    # Handle manufacturer
    # if device['platform'] in ('IOS-XE', 'IOS', 'NX-OS'):
    #     manu = 'Cisco'
    # existing_manu = get_manufacturers()
    # for ex_manu in existing_manu:
    #     if ex_manu['name'] == manu:
    #         manu_id = ex_manu['id']
    #     else:
    #         print("Something went wrong with getting Manu ID")

    # Handle Device Type
    print(nb.dcim.device_types.all())
    dev_type = input("Select type a Dev type from above: ")
    existing_types = get_dev_types()
    for ex_type in existing_types:
        if ex_type['name'] == dev_type:
            type_id = ex_type['id']
        else:
            print("Something went wrong with getting Dev Type ID")

    # GO
    try:
        results = nb.dcim.devices.create(name=hostname,
                                         device_role=role_id,
                                         device_type=type_id,
                                         site=site_id,
                                         status="active",
                                         serial=serial,
                                         tenant=ten_id
                                         )
    except Exception as err:
        results = err
    return Result(host=task.host, result=results)


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=device_creator)
    print_result(results)
