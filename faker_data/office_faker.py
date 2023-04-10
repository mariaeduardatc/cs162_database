from extensions import session
from databases.office_db import Office
from faker import Faker


def create_office(office_num):

    for i in range(office_num):
        fake = Faker()
        office = Office(**{
            "name": fake.company(),
            "phone": fake.phone_number()
            })

        session.add(office)
    
    session.commit()
