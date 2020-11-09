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

nr = InitNornir(config_file="config.yaml")


# def config_checker():
#     config_gen()


def get_inv_details(task):
    response = task.run(task=send_command,
                        command='show interfaces', severity_level=logging.DEBUG)
    results = response.scrapli_response.textfsm_parse_output()
    return Result(host=task.host, result=results)


if __name__ == "__main__":
    response = input("Do you want to gen a config first? (y/N): ")
    if response == "y":
        config_gen()
    results = nr.run(task=get_inv_details)
    print_result(results)
