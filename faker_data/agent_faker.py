from extensions import session
from databases.agent_db import Agent
from faker import Faker
import random

def create_agent(agents_num, office_num):
    """
        Creates a specified number of Agent instances with randomized data and saves them to the database.

    Parameters
    -----------
        - agents_num (int): The number of agents to create.
        - office_num (int): The total number of offices available for assigning an office to each agent.

    Returns
    ---------
        None
    """
    
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