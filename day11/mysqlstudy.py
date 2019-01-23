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
create_dep = '''create table departments(
dep_id int, 
dep_name varchar(20) not null unique, 
primary key(dep_id)
)'''
create_emp = '''create table employees(
emp_id int, 
emp_name varchar(20) not null, 
gender varchar(6), 
birth_date date, 
pho_num char(11) not null, 
dep_id int, 
email varchar(20), 
primary key(emp_id), 
foreign key(dep_id) references departments(dep_id)
)'''
create_sal = '''create table salary(
auto_id int,
date date,
emp_id int,
base_salary int,
awards int,
primary key(auto_id),
foreign key(emp_id) references employees(emp_id)
)'''
cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_sal)
cursor.close()
conn.close()
