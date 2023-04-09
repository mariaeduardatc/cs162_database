import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.house_db import House
from databases.sales_db import Sales

from faker import Faker

engine = create_engine('sqlite:///sales.db')
Base = declarative_base() 

Session = sessionmaker(bind=engine)
session = Session()

def create_sales(sales_num, house_num, buyers_num, agents_num):
    for i in range(sales_num):
        fake = Faker()
        house_id = random.choice([i + 1 for i in range(house_num)])
        house_price = session.query(House).filter_by(id=house_id).first().price
        sales = Sales(**{
            "name": fake.name(),
            "house_id": house_id,
            "buyer_id": random.choice([i + 1 for i in range(buyers_num)]),
            "agent_id": random.choice([i + 1 for i in range(agents_num)]),
            "price":  house_price,
            "date": fake.date()
            })
        
        # changing status of the sold house
        house_sold = session.query(House).filter_by(id=house_id).first()
        house_sold.sold = True
        session.commit()
        
        session.add(sales)
    session.commit()
