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
create_dep = '''CREATE TABLE departments(
dep_id INT, 
dep_name VARCHAR(20) NOT NULL UNIQUE, 
PRIMARY KEY(dep_id)
)'''
create_emp = '''CREATE TABLE employees(
emp_id INT, 
emp_name VARCHAR(20) NOT NULL, 
gender VARCHAR(6), 
birth_date DATE, 
pho_num CHAR(11) NOT NULL, 
dep_id INT, 
email VARCHAR(20), 
PRIMARY KEY(emp_id), 
FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
)'''
create_sal = '''CREATE TABLE salary(
auto_id INT,
date DATE,
emp_id INT,
base_salary INT,
awards INT,
primary KEY(auto_id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)'''
cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_sal)
cursor.close()
conn.close()
