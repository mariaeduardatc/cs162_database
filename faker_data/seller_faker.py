from extensions import session
from databases.seller_db import Seller

from faker import Faker


def create_seller(seller_num):
    for i in range(seller_num):
        fake = Faker()
        seller = Seller(**{
            "name": fake.name(),
            "email": fake.email()
        })
        
        session.add(seller)
    session.commit()