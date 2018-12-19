# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess as sp

ipaddr = ['8.8.8.8', '10.10.10.1', '87.250.250.242', '10.10.10.2', '217.69.139.201', '10.10.10.3']
avail = []
unavail = []


def check_ip_addresses(list_ip):
    for ip in list_ip:
        res = sp.run(['ping', '-c', '3', '-n', ip], stdout=sp.DEVNULL)
        if res.returncode == 0:
            avail.append(ip)
        else:
            unavail.append(ip)
    return avail, unavail



if __name__ == '__main__':
    print(check_ip_addresses(ipaddr))
