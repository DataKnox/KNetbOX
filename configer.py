from pypinger import pyping
import yaml


def config_gen():
    config = {
        'inventory': {
            'plugin': 'SimpleInventory',
            'options': {
                'host_file': 'inventory.yaml',
                'group_file': 'groups.yaml'
            }
        },
        'runner': {
            'plugin': 'threaded',
            'options': {
                'num_workers': 1
            }
        }
    }
    f = open('config.yaml', 'w')
    yaml.dump(config, f, allow_unicode=True)
    hosts = pyping()
    user = input("Username (default to cisco): ")
    if not user:
        user = 'cisco'
    password = input("Passowrd (default to cisco): ")
    if not password:
        password = 'cisco'
    hosts_list = {}
    for host in hosts:
        host_data = {
            'hostname': host,
            'username': user,
            'password': password,
            'groups': ['cisco_group']
        }
        hosts_list[host] = host_data
    print(yaml.dump(hosts_list))
    f = open('inventory.yaml', 'w')
    yaml.dump(hosts_list, f, allow_unicode=True)
    group = {
        'cisco_group': {
            'username': 'cisco',
            'password': 'cisco',
            'connection_options': {
                'scrapli': {
                    'platform': 'cisco_iosxe',
                    'port': 22,
                    'extras': {'ssh_config_file': True, 'auth_strict_key': False}
                },
                'scrapli_netconf': {
                    'port': 830,
                    'extras': {'ssh_config_file': True, 'auth_strict_key': False}
                }
            }
        }
    }
    f = open('groups.yaml', 'w')
    yaml.dump(group, f, allow_unicode=True)
