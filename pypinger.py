import subprocess
import ipaddress
from subprocess import Popen, PIPE
import platform
import argparse


def pyping():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--subnet', type=str,
                        dest="subnet", help='Provide topology name.')
    args = parser.parse_args()
    if args.subnet:
        subnet = args.subnet
    else:
        subnet = input("Please enter the network: ")

    alive_hosts = []

    current_os = platform.system().lower()
    # print(current_os)

    network = ipaddress.ip_network(subnet)

    if current_os == "windows":
        parameter = "-n"
    else:
        parameter = "-c"
    for i in network.hosts():
        i = str(i)
        toping = subprocess.Popen(['ping', parameter, '5', i], stdout=PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            print(i, ': !!!!!')
            alive_hosts.append(i)

        else:
            print(i, ': .....')
    return alive_hosts


if __name__ == "__main__":
    pyping()
