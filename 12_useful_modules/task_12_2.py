# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''


import subprocess as sp

ip_input = input('Enter IP: ')

ip = ip_input.split('.')

ipaddr = []

if len(ip) == 4 and ip[3].isdigit():
    ipaddr.append(ip_input)

elif len(ip) == 4 and '-' in ip[3]:
    octet = ip[3].split('-')
    o_part1 = int(octet[0])
    o_part2 = int(octet[1])
    ip_to_list = ip[:3]
 
    for i in range(o_part1, o_part2 + 1):
        ip_to_list.append(str(i))
        res_ip = '.'.join(ip_to_list)
        ipaddr.append(res_ip)
        ip_to_list.pop(-1)

elif len(ip) == 7:
    two_ip = ip_input.split('-')
    ip1 = two_ip[0].split('.')
    ip2 = two_ip[1].split('.')
    ipaddr.extend(two_ip) 
    for i in range(int(ip1[-1])+1, int(ip2[-1])):
        ip_to_list = ip1[:3]
        ip_to_list.append(str(i))
        res_ip = '.'.join(ip_to_list)
        ipaddr.append(res_ip)
        ip_to_list.pop(-1)

else:
    print('Wrong ip/range')


avail = []
unavail = []


def check_ip_addresses(list_ip):
    for ip in list_ip:
        print('Check available ip {}...'.format(ip))
        res = sp.run(['ping', '-c', '3', '-n', ip], stdout=sp.DEVNULL)
        if res.returncode == 0:
            avail.append(ip)
        else:
            unavail.append(ip)
    return avail, unavail



if __name__ == '__main__':
    print(check_ip_addresses(ipaddr))
