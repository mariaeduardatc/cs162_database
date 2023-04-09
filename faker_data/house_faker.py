import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.house_db import House

from faker import Faker

# to create the db
engine = create_engine('sqlite:///house.db')
Base = declarative_base()
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_house(house_num, agents_num):
    for i in range(house_num):
        fake = Faker()
        house = House(**{
            "name": fake.name(),
            "bedrooms": fake.random_int(min=1, max=50),
            "bathrooms": fake.random_int(min=1, max=50),
            "price": fake.random_int(min=1000, max=1000000000),
            "zipcode": fake.random_int(min=10000, max=99999),
            "date_listing": fake.date_this_decade(),
            "sold": False,
            "seller_id": random.choice([i + 1 for i in range(agents_num)])
            })
        
        session.add(house)

    session.commit()
