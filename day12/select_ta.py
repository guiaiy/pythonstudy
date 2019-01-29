#!/usr/bin/env python3
from sqlalchemy import or_

from day12.tables import *

session = Session()

q1 = session.query(Departments.dep_name, Departments.dep_id) \
    .filter(or_(Departments.dep_id == 1, Departments.dep_id == 2))
# print(q1.all())
for m, q in q1:
    print('%s: %s' % (m, q))
