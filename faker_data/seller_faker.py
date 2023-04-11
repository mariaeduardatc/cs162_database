from extensions import session
from databases.seller_db import Seller

from faker import Faker


def create_seller(seller_num):
    for i in range(seller_num):
        fake = Faker()
        seller = Seller(**{
            "name": fake.name(),
            "phone": fake.phone_number()
        })
        
        session.add(seller)
    session.commit()