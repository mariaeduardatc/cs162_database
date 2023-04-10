from extensions import session
from databases.agent_db import Agent
from faker import Faker
import random

def create_agent(agents_num, office_num):
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
