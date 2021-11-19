import ipaddress


def main():
    # Создание IPv4-адреса - функция ip_address()
    ipv4 = ipaddress.ip_address('192.168.0.1')
    print(ipv4)
    # Проверка диапазона, к которому принадлежит адрес - атрибуты is_loopback,
    # is_multicast, is_reserved, is_private
    print(ipv4.is_loopback)
    print(ipv4.is_multicast)
    print(ipv4.is_reserved)
    print(ipv4.is_private)


def compare():
    # Операции с объектом адреса
    ip1 = ipaddress.ip_address('192.168.1.0')
    ip2 = ipaddress.ip_address('192.168.1.255')
    if ip2 > ip1:
        print(True)
    print(str(ip1))
    print(int(ip1))
    print(ip1 + 5)
    print(ip1 - 5)


def network():
    # Создание объекта, описывающего сеть - функция ip_network()
    subnet = ipaddress.ip_network('80.0.1.0/28')
    ba = subnet.broadcast_address
    print(ba)
    # Просмотр всех хостов для объекта-сети
    for host in subnet.hosts():
        print(host)
    # print(list(subnet.hosts()))

    # Разбиение сети на подсети
    print(list(subnet.subnets()))
    # Обращение к любому адресу в сети
    print(subnet[1])
    # Создание интерфейса
    ipv4_int = ipaddress.ip_interface('10.0.1.1/24')
    # Получение адреса
    print(ipv4_int.ip)
    # Получение маски
    print(ipv4_int.netmask)
    # Получение сети
    print(ipv4_int.network)


ip_1 = '10.0.1.1/24'
ip_2 = '10.0.1.0/24'


def ip_network_check(ip_addr):
    try:
        ipaddress.ip_network(ip_addr)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    network()
    print("Программа запершена")

    print(ip_network_check(ip_1))
    print(ip_network_check(ip_2))
