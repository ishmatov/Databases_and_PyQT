"""2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона. Меняться должен только
последний октет каждого адреса. По результатам проверки должно выводиться соответствующее сообщение. """
import ipaddress
from helper import accessible_ip


def host_range_ping(network):
    subnet = ipaddress.ip_network(network)
    for host in subnet.hosts():
        print(f'{str(host)} - Узел доступен' if accessible_ip(host) else f'{str(host)} - Узел недоступен')


if __name__ == "__main__":
    host_range_ping('80.0.1.0/28')
