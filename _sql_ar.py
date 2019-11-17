from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String,Column,Integer,ForeignKey

engine=create_engine("mysql+mysqldb://root:44070423@localhost:3306/flask_DB")

Session=sessionmaker(bind=engine)

Base=declarative_base()
#
# class Student(Base):
#     __tablename__="students"
#     Sno=Column(String(10),primary_key=True)
#     Sname=Column(String(20),nullable=False,unique=True,index=True)
#     Ssex = Column(String(2), nullable=False)
#     Sage = Column(Integer, nullable=False)
#     Sdept = Column(String(20))
#
#     def __repr__(self):
#         return "<Student>{}:{}".format(self.Sname,self.Sno)
#
# Base.metadata.create_all(engine)
# session=Session()
# student = Student(Sno='10001',Sname='Frnak',Ssex='M',Sage=22,Sdept='SFS')
# session.add(student)
# session.commit()
# session.close()
# print(session.query(Student).filter(Student.Sname == 'Frnak').first())
# target=session.query(Student).get("10001")
# session.delete(target)
# session.commit()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(20),nullable=False)

    addresses = relationship('Address')
class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer,primary_key=True)
    address = Column(String(20),nullable=False)
    user_id = Column(Integer,ForeignKey('users.id')) #请注意，设置外键的时候用的是表名.字段名。其实在表和表类的抉择中，只要参数是字符串，往往是表名；如果是对象则是表类对象。

    user = relationship('Uszer')