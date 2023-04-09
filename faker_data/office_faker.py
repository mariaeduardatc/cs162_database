from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.office_db import Office

from faker import Faker

def create_office(office_num):
    engine = create_engine('sqlite:///office.db')
    Base = declarative_base() 
    Base.metadata.create_all(bind=engine) 
    Session = sessionmaker(bind=engine)
    session = Session()

    for i in range(office_num):
        fake = Faker()
        office = Office(**{
            "name": fake.company(),
            "phone": fake.phone_number()
            })

        session.add(office)
    
    session.commit()