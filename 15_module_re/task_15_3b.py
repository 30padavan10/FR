# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

from sys import argv
import re

file = argv[1]

regex = ('interface (?P<inter>\S+)'
         '|.*ip address (?P<ip>(\d+\.)+\d+) (?P<mask>(\d+\.)+\d+).*')


def parse_cfg(file, reg):
    with open(file) as src:
        result = {}
        for line in src:
            res = re.search(reg, line)
            if res:
                if res.lastgroup == 'inter':
                    interface = res.group('inter')
                elif res.lastgroup == 'mask':
                    if result.get(interface):
                        result[interface].append(res.group('ip', 'mask'))
                    else:
                        result[interface] = []
                        result[interface].append(res.group('ip', 'mask'))
        print(result)



if __name__ == '__main__':
    parse_cfg(file, regex)

