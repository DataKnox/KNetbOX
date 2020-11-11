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


nb = pynetbox.api(
    'http://10.10.21.196:8000',
    token='0123456789abcdef0123456789abcdef01234567')

site = print(nb.dcim.sites.get(name="Homelab"))
print(site._full_cache)
print(nb.dcim.device_roles.all())
print(nb.dcim.manufacturers.all())
print(nb.dcim.device_types.all())


def device_creator(task):
    device = task.run(task=get_inv_details,
                      severity_level=logging.DEBUG)[0].result
    print(device)
    hostname = device['hostname']
    print(nb.dcim.sites.all())
    site = input("Choose a site from above list: ")
    role = 'Virtual'
    for int in device['interfaces']:
        if int['media'] != 'Virtual':
            role = int['media']
    if device['platform'] in ('IOS-XE', 'IOS', 'NX-OS'):
        manu = 'Cisco'
    print(nb.dcim.device_types.all())
    dev_type = input("Select a device type from above: ")
    try:
        results = nb.dcim.devices.create(name=hostname,
                                         device_role=role,
                                         device_type=dev_type,
                                         site=site,
                                         status="Active"
                                         )
    except Exception as err:
        results = err
    return Result(host=task.host, result=results)


if __name__ == "__main__":
    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=device_creator)
    print_result(results)
