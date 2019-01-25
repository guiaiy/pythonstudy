#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 连接指定库 用户名：密码@服务器/数据库？参数
engine = create_engine(
    'mysql+pymysql://root:123456@127.0.0.1/songda?charset=utf8',
    encoding='utf8',
    # echo=True  # 调试信息，生产环境不用打开
)
Base = declarative_base()  # 生成ORM需要的基类
Session = sessionmaker(bind=engine)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '<name: %s>' % self.emp_name


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    base_salary = Column(Integer)
    award = Column(Integer)

    def __str__(self):
        return '<id: %s, salary: %s>' % (self.emp_id, self.base_salary + self.award)


class Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return '<部门： %s>' % self.dep_name


if __name__ == '__main__':
    Base.metadata.create_all(engine)
