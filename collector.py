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


# def config_checker():
#     config_gen()


def get_inv_details(task):
    response = task.run(task=send_command,
                        command='show interfaces', severity_level=logging.DEBUG)
    int_results = response.scrapli_response.textfsm_parse_output()
    ver_response = task.run(
        task=send_command, command='show version', severity_level=logging.DEBUG)
    ver_results = ver_response.scrapli_response.textfsm_parse_output()
    results = {}
    results['hostname'] = ver_results[0]['hostname']
    results['platform'] = ver_results[0]['rommon']
    results['serial'] = ver_results[0]['serial'][0]
    results['interfaces'] = []
    for int in int_results:
        interface = {}
        interface['name'] = int['interface']
        interface['mac'] = int['bia']
        interface['ip'] = int['ip_address']
        interface['media'] = int['media_type']
        interface['active'] = int['link_status']
        results['interfaces'].append(interface)
    return results


if __name__ == "__main__":
    response = input("Do you want to gen a config first? (y/N): ")
    if response == "y":
        config_gen()
    nr = InitNornir(config_file="config.yaml")
    results = nr.run(task=get_inv_details)
    print_result(results)
