#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/jwy?charset=utf8',
    encoding='utf8'
)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '<name: %s>' % self.emp_name


class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True, autoincrement=True)
    dep_name = Column(String(20))

    def __str__(self):
        return '<name: %s>' % self.dep_name


class Salary(Base):
    __tablename__ = 'salaryinfo'
    autoid = Column(Integer, primary_key=True, autoincrement=True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    date = Column(Date)
    basic = Column(Integer)
    award = Column(Integer)

    def __str__(self):
        return '<salary: %s>' % self.basic + self.award


if __name__ == '__main__':
    Base.metadata.create_all(engine)
