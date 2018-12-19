# -*- coding: utf-8 -*-
'''
Задание 15.1a

Напишите регулярное выражение, которое отобразит строки
с интерфейсами 0/1 и 0/3 из вывода sh ip int br.

Проверьте регулярное выражение, используя скрипт, который был создан в задании 15.1,
и файл sh_ip_int_br.txt.

В этом файле нужно написать только регулярное выражение.

'''

from sys import argv
import re
import task_15_1b as task

regex = '\w+0/[13] +.*'

fil = argv[1]

def parse_sh(file, reg):
    with open(file) as src:
        for line in src:
            match = re.match(reg, line)
            if match:
                print(match.group())


if __name__ == '__main__':
    parse_sh(fil, task.regex)
