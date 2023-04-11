from extensions import session
from databases.office_db import Office
from faker import Faker


def create_office(office_num):
    """
        Creates a specified number of Agent instances with randomized data and saves them to the database.

    Parameters
    ----------
        - agents_num (int): The number of agents to create.
        - office_num (int): The total number of offices available for assigning an office to each agent.

    Returns
    -------
        None
    """
    # data normalization -> columns are directly connected to the id
    for i in range(office_num):
        fake = Faker()
        office = Office(**{
            "name": fake.company(),
            "phone": fake.phone_number()
            })

        session.add(office)
    
    session.commit()
