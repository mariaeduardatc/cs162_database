import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base
from databases.house_db import House

from databases.sales_db import Sales


from faker import Faker

def create_sales(holder, house_num, buyer_num, agent_num):
    for i in range(holder):
        fake = Faker()
        house_id = random.choice([i + 1 for i in range(house_num)])
        sales = Sales(**{
            "name": fake.name(),
            "house_id": house_id,
            "buyer_id": random.choice([i + 1 for i in range(buyer_num)]),
            "agent_id": random.choice([i + 1 for i in range(agent_num)]),
            "price":  session.query(House).filter_by(id=house_id).first().price,
            "date": fake.date()
            })
        
        # to create the db
        engine = create_engine('sqlite:///sales.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(sales)
        session.commit()