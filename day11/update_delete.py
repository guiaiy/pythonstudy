#!/usr/bin/env python3
from day11.tables import *

session = Session()
# sales = Departments(dep_id=6, dep_name='sales')
# session.add(sales)  # insert
# sale = session.query(Departments).filter(Departments.dep_id == 6)  # select
# sale.one().dep_name = 'sale'  # update
# session.delete(sale.one())  # delete
session.commit()
