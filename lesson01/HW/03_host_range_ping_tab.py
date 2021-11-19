"""3. Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном
случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль
tabulate). Таблица должна состоять из двух колонок и выглядеть примерно так:

Reachable
10.0.0.1
10.0.0.2

Unreachable
10.0.0.3
10.0.0.4
"""
from helper import *
from tabulate import tabulate


def host_range_ping_tab(network):
    subnet = ipaddress.ip_network(network)
    tab = {"Reachable": [], "Unreachable": []}
    for host in subnet.hosts():
        if accessible_ip(host):
            tab["Reachable"].append(str(host))
        else:
            tab["Unreachable"].append(str(host))
        print(".", end="")
    print()
    print(tabulate(tab, headers='keys'))


if __name__ == "__main__":
    host_range_ping_tab('80.0.1.0/28')
