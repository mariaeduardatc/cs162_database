from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.agent_db import Agent

from faker import Faker
import random

def create_agent(agents_num, office_num):
    # to create the db
    engine = create_engine('sqlite:///agent.db')
    Base = declarative_base() 

    Base.metadata.create_all(bind=engine) 

    Session = sessionmaker(bind=engine)
    session = Session()

    for _ in range(agents_num):
        fake = Faker()
        agent = Agent(**{
            "name": fake.name(),
            "email": fake.email(),
            "sales": fake.random_int(min=0, max=1000),
            "office_id": random.choice([i + 1 for i in range(office_num)])
            })
        
        session.add(agent)

    session.commit()
