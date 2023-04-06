from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

from databases.agent_db import Agent


from faker import Faker
import random

def createAgents(numBuyers, numOffices):
    for i in range(numBuyers):
        fake = Faker()
        agent = Agent(**{
            "name": fake.name(),
            "email": fake.email(),
            "sales": fake.integer(), # change this
            "office_id": random.choice([i + 1 for i in range(numOffices)])
            })
        
        # to create the db
        engine = create_engine('sqlite:///buyer.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(agent)
        session.commit()