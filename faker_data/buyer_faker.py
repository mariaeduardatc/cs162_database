from extensions import session
from databases.buyer_db import Buyer
from faker import Faker

def create_buyer(buyers_num):
    for _ in range(buyers_num):
        fake = Faker()
        buyer = Buyer(**{
            "name": fake.name(),
            "email": fake.email()
        })

        session.add(buyer)
    session.commit()
