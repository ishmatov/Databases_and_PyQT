import ipaddress
import socket
import subprocess


def get_ip(host):
    try:
        return ipaddress.ip_address(host)
    except ValueError:
        try:
            return ipaddress.ip_address(socket.gethostbyname(host))
        except:
            print(f"{host} - Не верное имя узла")
            return False


def accessible_ip(ip):
    with subprocess.Popen(['ping', str(ip), '-n', '1'],
                          stdout=subprocess.PIPE) as process:
        data = process.communicate()
        answer = data[0].decode('CP866')
        if 'Заданный узел недоступен' in answer:
            return False
        return True
