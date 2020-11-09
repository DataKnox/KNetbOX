import subprocess
import ipaddress
from subprocess import Popen, PIPE


def test_hosts():
    alive_hosts = []
    subnet = input("Please enter the network: ")
    network = ipaddress.ip_network(subnet)
    for i in network.hosts():
        i = str(i)
        toping = subprocess.Popen(['ping', '-c', '1', i], stdout=PIPE)
        output = toping.communicate()[0]
        hostalive = toping.returncode
        if hostalive == 0:
            print(i, 'is reachable')
            alive_hosts.append(i)

        else:
            print(i, 'is down')
    return alive_hosts
