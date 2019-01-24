#!/usr/bin/env python3
from sqlalchemy import or_, and_

from day11.tables import Employees, Departments, Session

session = Session()
query1 = session.query(Departments)
query2 = session.query(Employees)
query3 = session.query(Employees.emp_name, Employees.email)
query4 = session.query(Employees.emp_name, Employees.email, Employees.dep_id) \
    .filter(and_(Employees.dep_id == 2, Employees.email.like('%@qq.com')))
query5 = session.query(Employees.emp_name, Employees.email, Employees.dep_id) \
    .filter(or_(Employees.dep_id == 2, Employees.email.like('%@qq.com')))
query6 = session.query(Employees.emp_name, Employees.email) \
    .filter(Employees.emp_id == 2018002)
query7 = session.query(Employees.emp_name, Employees.email) \
    .filter(Employees.dep_id == 2) \
    .filter(Employees.email.like('%@qq.com'))
query8 = session.query(Employees).filter(Employees.dep_id == 2)
query9 = session.query(Employees.emp_name, Departments.dep_name) \
    .join(Departments)
query10 = session.query(Departments.dep_name, Employees.emp_name) \
    .join(Employees)
# print(query1)
# print(query1.all())
# for dep in query1:n
#     print(dep)
# for dep in query1:
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
# for emp in query2:
#     print(emp, end=' ')
# print()
# for emp in query2:
#     print('id: %s, name: %s, email: %s, dep_id: %s' % (emp.emp_id, emp.emp_name, emp.email, emp.dep_id))
# print(query3.all())
# # for name, email in query3:
# #     print('%s: %s' % (name, email))
# print(query7.all())

# print(query4)
# for name, email, dep_id in query4:
#     print('%s: %s %s' % (name, email, dep_id))

# print(query5)
# for name, email, dep_id in query5:
#     print('%s: %s %s' % (name, email, dep_id))
# print(query5.first())
# print(query6.one())
# print(query8.count())
print(query9.all())
print(query10.all())
