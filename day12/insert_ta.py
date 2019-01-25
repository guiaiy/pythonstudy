#!/usr/bin/env python3
from day12.tables import *

session = Session()

# sale = Departments(dep_id=6, dep_name='sale')
# session.add(sale)
# session.commit()
# hr = Departments(dep_id=1, dep_name='hr')
# ops = Departments(dep_id=2, dep_name='ops')
# dev = Departments(dep_id=3, dep_name='dev')
# qs = Departments(dep_id=4, dep_name='qs')
# fn = Departments(dep_id=5, dep_name='fn')
# session.add_all([hr, ops, dev, qs, fn])
# session.commit()

tc = Employees(emp_id=2018001, emp_name='tc', dep_id=1)
sd = Employees(emp_id=2018002, emp_name='sd', dep_id=2)
jwy = Employees(emp_id=2018003, emp_name='jwy', dep_id=3)
tr = Employees(emp_id=2018004, emp_name='tr', dep_id=3)
lz = Employees(emp_id=2018005, emp_name='lz', dep_id=4)
wcc = Employees(emp_id=2018006, emp_name='wcc', dep_id=2)
rtp = Employees(emp_id=2018007, emp_name='rtp', dep_id=5)
session.add_all([tc, sd, jwy, tr, lz, wcc, rtp])
session.commit()
session.close()