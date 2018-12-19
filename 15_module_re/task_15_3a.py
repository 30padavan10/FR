# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

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
                    result.update({interface:(res.group('ip', 'mask'))})
        print(result)



if __name__ == '__main__':
    parse_cfg(file, regex) 
