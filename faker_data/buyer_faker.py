from extensions import session
from databases.buyer_db import Buyer
from faker import Faker

def create_buyer(buyers_num):
    """
        Create a specified number of buyers and add them to the database.

    Parameters
    ----------
        - buyers_num (int) : The number of buyers to create.

    Returns
    -------
        None
    """
    for _ in range(buyers_num):
        fake = Faker()
        buyer = Buyer(**{
            "name": fake.name(),
            "email": fake.email()
        })

        session.add(buyer)
    session.commit()
