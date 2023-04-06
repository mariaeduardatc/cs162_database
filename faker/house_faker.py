import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.house_db import House


from faker import Faker

def create_house(holder, num_agents):
    for i in range(holder):
        fake = Faker()
        house = House(**{
            "name": fake.name(),
            "bedrooms": fake.integer(),
            "bathrooms": fake.integer(),
            "price": fake.integer(),
            "zipcode": fake.integer(),
            "date_listing": fake.integer(),
            "sold": False,
            "seller_id": random.choice([i + 1 for i in range(num_agents)])
            })
        
        # to create the db
        engine = create_engine('sqlite:///buyer.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(house)
        session.commit()