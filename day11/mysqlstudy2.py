#!/usr/bin/env python3
import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456',
    db='nsd1808',
    charset='utf8'
)
cursor = conn.cursor()
# create_dep = '''create table departments(
# dep_id int,
# dep_name varchar(20) not null unique,
# primary key(dep_id)
# )'''
# create_emp = '''create table employees(
# emp_id int,
# emp_name varchar(20) not null,
# gender varchar(6),
# birth_date date,
# pho_num char(11) not null,
# dep_id int,
# email varchar(20),
# primary key(emp_id),
# foreign key(dep_id) references departments(dep_id)
# )'''
# create_sal = '''create table salary(
# auto_id int,
# date date,
# emp_id int,
# base_salary int,
# awards int,
# primary key(auto_id),
# foreign key(emp_id) references employees(emp_id)
# )'''
# insert1 = 'insert into departments values(%s, %s)'
# cursor.execute(insert1, (1, 'HR'))
# deps = [(2, 'yunwei'), (3, 'kaifa'), (4, 'ceshi')]
# cursor.executemany(insert1, deps)
# insert2 = 'insert into employees values(%s, %s, %s, %s, %s, %s, %s)'
# emps = [
#     (20180001, 'songda', 'male', 19900508, '13823550417', 2, '531456111@qq.com'),
#     (20180002, 'jwy', 'male', 19900509, '13215546521', 3, '255431221@qq.com')
# ]
# cursor.executemany(insert2, emps)
# conn.commit()
query1 = 'select * from departments order by dep_id'
cursor.execute(query1)
# result1 = cursor.fetchone()
# print(result1)
# print('*' * 30)
# result2 = cursor.fetchmany(2)
# print(result2)
# print('*' * 30)
# result3 = cursor.fetchall()
# print(result3)
cursor.scroll(1, mode='absolute')
print(cursor.fetchone())
cursor.scroll(1, mode='relative')
print(cursor.fetchone())
cursor.scroll(2, mode='absolute')
print(cursor.fetchone())
cursor.close()
conn.close()