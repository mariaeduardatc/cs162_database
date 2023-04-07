import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.house_db import House


from faker import Faker

def create_house(house_num, agents_num):
    for i in range(house_num):
        fake = Faker()
        house = House(**{
            "name": fake.name(),
            "bedrooms": fake.integer(),
            "bathrooms": fake.integer(),
            "price": fake.integer(),
            "zipcode": fake.integer(),
            "date_listing": fake.integer(),
            "sold": False,
            "seller_id": random.choice([i + 1 for i in range(agents_num)])
            })
        
        # to create the db
        engine = create_engine('sqlite:///house.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(house)
        session.commit()