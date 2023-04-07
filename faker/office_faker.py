from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.office_db import Office


from faker import Faker

def create_office(holder):
    for i in range(holder):
        fake = Faker()
        office = Office(**{
            "name": fake.name(),
            "phone": fake.integer()
            })
        
        # to create the db
        engine = create_engine('sqlite:///office.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(office)
        session.commit()