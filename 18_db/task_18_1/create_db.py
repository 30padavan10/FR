# -*- coding: utf-8 -*-
"""
Задание 18.1

create_db.py
* сюда должна быть вынесена функциональность по созданию БД:
 * должна выполняться проверка наличия файла БД
 * если файла нет, согласно описанию схемы БД в файле dhcp_snooping_schema.sql,
   должна быть создана БД (БД отличается от примера в разделе)

В БД теперь две таблицы (схема описана в файле dhcp_snooping_schema.sql):
 * switches - в ней находятся данные о коммутаторах
 * dhcp - эта таблица осталась такой же как в примере, за исключением поля switch
  * это поле ссылается на поле hostname в таблице switches

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
"""
import sqlite3
import os


db_filename = 'dhcp_snooping.db'
schema_filename = 'dhcp_snooping_schema.sql'



def open_schema(schema_filename):
    with open(schema_filename) as src:
        schema = src.read()
    return schema



def exist_db(db_filename, schema):
    db_exists = os.path.exists(db_filename)

    if not db_exists:
        conn = sqlite3.connect(db_filename)
        with conn:
            conn.executescript(schema)
        print('DB creating')
    else:
        print('DB created')


if __name__ == '__main__':
    exist_db(db_filename, open_schema(schema_filename))
