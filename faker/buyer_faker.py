from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.buyer_db import Buyer


from faker import Faker

def create_buyer(buyers_num):
    for _ in range(buyers_num):
        fake = Faker()
        buyer = Buyer(**{
            "name": fake.name(),
            "email": fake.email()
            })
        
        # to create the db
        engine = create_engine('sqlite:///buyer.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(buyer)
        session.commit()