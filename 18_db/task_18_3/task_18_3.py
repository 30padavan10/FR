# -*- coding: utf-8 -*-
'''
Задание 18.3

В прошлых заданиях информация добавлялась в пустую БД.
В этом задании, разбирается ситуация, когда в БД уже есть информация.

Скопируйте скрипт add_data.py и попробуйте выполнить его повторно, на существующей БД.
Должна возникнуть ошибка.

При создании схемы БД, было явно указано, что поле MAC-адрес, должно быть уникальным.
Поэтому, при добавлении записи с таким же MAC-адресом, возникает ошибка.

Но, нужно каким-то образом обновлять БД, чтобы в ней хранилась актуальная информация.

Например, можно каждый раз, когда записывается информация,
предварительно просто удалять всё из таблицы dhcp.

Но, в принципе, старая информация тоже может пригодиться.

Поэтому, мы будем делать немного по-другому.
Создадим новое поле active, которое будет указывать является ли запись актуальной.

Поле active должно принимать такие значения:
* 0 - означает False. И используется для того, чтобы отметить запись как неактивную
* 1 - True. Используется чтобы указать, что запись активна

Каждый раз, когда информация из файлов с выводом DHCP snooping добавляется заново,
надо пометить все существующие записи (для данного коммутатора), как неактивные (active = 0).
Затем можно обновлять информацию и пометить новые записи, как активные (active = 1).


Таким образом, в БД останутся и старые записи, для MAC-адресов, которые сейчас не активны,
и появится обновленная информация для активных адресов.

Новая схема БД находится в файле dhcp_snooping_schema.sql

Измените скрипт add_data.py таким образом, чтобы выполнялись новые условия и заполнялось поле active.

Код в скрипте должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.

> Для проверки корректности запроса SQL, можно выполнить его в командной строке, с помощью утилиты sqlite3.

Для проверки задания и работы нового поля, попробуйте удалить пару строк
из одного из файлов с выводом dhcp snooping.
И после этого проверить, что удаленные строки отображаются в таблице как неактивные.

'''
from sys import argv
import sqlite3
import glob
import re
import os

def create_db():
    with open('dhcp_snooping_schema.sql') as src:
        schema = src.read()
    conn = sqlite3.connect('dhcp_snooping2.db')
    with conn:
        conn.executescript(schema)
    print('DB created')

def add_data():
    exists = os.path.exists('dhcp_snooping2.db')
    if exists:
        conn = sqlite3.connect('dhcp_snooping2.db')
        switch_files = glob.glob('*dhcp_snooping.txt') 
        regex = '(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)'

        for switch in switch_files:
            result = []
            with open(switch) as src:
                mac_table = src.read()
            matches = re.finditer(regex, mac_table)
            for match in matches:
                line = list(match.groups())
                line.append(switch[:switch.index('_dhcp')])
                result.append(line)

            query_up = 'update dhcp set active=0 where switch=?'
            query_insert = 'replace into dhcp (mac, ip, vlan, interface, switch, active) values (?, ?, ?, ?, ?, 1)'

            with conn:
                try:
                    conn.execute(query_up, (switch[:switch.index('_dhcp')],))
                except sqlite3.OperationalError:
                    pass
                for row in result:
                    conn.execute(query_insert, row)

        print('data added')
    else:
        print('for start you need create db')

def select_param_db():
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']

    key, value = argv[1:]
    keys.remove(key)
    conn = sqlite3.connect('dhcp_snooping2.db')
    with conn:
        query = 'select * from dhcp where {} = ? and active = ?'.format(key)
        conn.row_factory = sqlite3.Row
        result_act = conn.execute(query, (value, 1))
        result_inact = conn.execute(query, (value, 0))

        print('-'*40)
        print('active')
        print('-'*40)

        for row in result_act:
           for k in keys:
               print('{:15} {}'.format(k, row[k]))
           print('-'*40)

        print('-'*40)
        print('inactive')
        print('-'*40)

        for row in result_inact:
           for k in keys:
               print('{:15} {}'.format(k, row[k]))
           print('-'*40) 


def select_db():
    conn = sqlite3.connect('dhcp_snooping2.db')
    query = 'select * from dhcp'
    result = conn.execute(query)
    active = []
    inactive = []
    for row in result:
        if row[-1] == 1:
            active.append(list(row))
        else:
            inactive.append(list(row))
    print('-'*80)
    print('active')
    print('-'*80)
    for i in active:
        print('{:20} {:20} {:10} {:20} {:5} {:5}'.format(*i))
    print('-'*80)
    print('inactive')
    print('-'*80)
    for i in inactive:
        print('{:20} {:20} {:10} {:20} {:5} {:5}'.format(*i))
    print('-'*80)

if __name__ == '__main__':
    if len(argv) == 2:
        command = input('Enter CREATE to create, enter ADD to add: ')
        if command == 'CREATE':
            create_db()
        elif command == 'ADD':
            add_data()
    elif len(argv) == 3:
        select_param_db()
    elif len(argv) == 1:
        select_db()
    else:
        print('Incorrect enter')
