from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.seller_db import Seller


from faker import Faker

def create_seller(seller_num):
    for i in range(seller_num):
        fake = Faker()
        sellers = Seller(**{
            "name": fake.name(),
            "email": fake.email()
        })
        
        # to create the db
        engine = create_engine('sqlite:///seller.db')
        engine.connect()

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(sellers)
        session.commit()