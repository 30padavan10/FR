# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(source_file):
    res_access = {}
    res_trunk = {}
    with open(source_file) as src:
        for line in src:
            if 'Ethernet' in line:
                intf = line.split()[-1]
            elif 'mode access' in line:
                res_access.update({intf:'1'})      #При каждом совпадении добавляем в словарь порт со значением влан 1
            elif 'access vlan' in line:
                vlan = line.split()[-1]
                res_access[intf] = vlan     #Если после mode access идет allowed vlan, то для порта меняем значение влан
            elif 'allowed vlan' in line:
                vlan = line.split()[-1].split(',')
                res_trunk.update({intf:vlan})
    print(res_access)
    print(res_trunk)
    return res_access, res_trunk


get_int_vlan_map('config_sw2.txt')
