from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import Session, relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///one-to-one.db')

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

class ContactInfo(Base):
    __tablename__ = 'contact_info'

    id = Column(Integer(), primary_key=True)
    phone = Column(String())
    employee_id = Column(Integer(), ForeignKey('employee.id'))
    employee = relationship('Employee', backref=backref('employee', uselist=False), back_populates='contact_info')


def create():
    # Base.metadata.create_all(engine)
    with Session(engine) as session:
        info = ContactInfo(
            phone='555-555-5555',
            employee=Employee(
                name='jane doe'
            )
        )
        session.add(info)
        session.commit()


if __name__ == '__main__':
    with Session(engine) as session:
        c = session.query(ContactInfo).first()
        print(c.phone, c.employee.name)
    
        
