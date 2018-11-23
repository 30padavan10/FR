# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(source_file):
    res_access = {}
    res_trunk = {}
    with open(source_file) as src:
        for line in src:
            if 'Ethernet' in line:
                intf = line.split()[-1]
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                res_access.update({intf:vlan})
            elif 'allowed vlan' in line:
                vlan = line.split()[-1].split(',')
                res_trunk.update({intf:vlan}) 
    print(res_access)
    print(res_trunk)
    return res_access, res_trunk


get_int_vlan_map('config_sw1.txt')
