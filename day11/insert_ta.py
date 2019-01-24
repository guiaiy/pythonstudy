#!/usr/bin/env python3
from day11 import tables

session = tables.Session()

sale = tables.Departments(dep_id=6, dep_name='sale')
session.add(sale)
session.commit()
# hr = tables.Departments(dep_id=1, dep_name='hr')
# ops = tables.Departments(dep_id=2, dep_name='ops')
# dev = tables.Departments(dep_id=3, dep_name='dev')
# qs = tables.Departments(dep_id=4, dep_name='qs')
# fn = tables.Departments(dep_id=5, dep_name='fn')
# session.add_all([hr, ops, dev, qs, fn])
# session.commit()

# tc = tables.Employees(emp_id=2018001, emp_name='tc', email='abfdsc@qq.com', dep_id=1)
# sd = tables.Employees(emp_id=2018002, emp_name='sd', email='abfsdc@qq.com', dep_id=2)
# jwy = tables.Employees(emp_id=2018003, emp_name='jwy', email='afdbc@qq.com', dep_id=3)
# tr = tables.Employees(emp_id=2018004, emp_name='tr', email='abfdsc@qq.com', dep_id=3)
# lz = tables.Employees(emp_id=2018005, emp_name='lz', email='abcsd@qq.com', dep_id=4)
# wcc = tables.Employees(emp_id=2018006, emp_name='wcc', email='abfac@qq.com', dep_id=2)
# rtp = tables.Employees(emp_id=2018007, emp_name='rtp', email='abfadfc@qq.com', dep_id=5)
# session.add_all([tc, sd, jwy, tr, lz, wcc, rtp])
# session.commit()
session.close()