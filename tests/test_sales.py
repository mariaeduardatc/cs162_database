import unittest
from datetime import date
from databases.sales_db import Sales
from databases.house_db import House
from databases.buyer_db import Buyer
from databases.agent_db import Agent
from databases.office_db import Office
from extensions import Base
from tests.tests_extensions import session, engine

class TestSales(unittest.TestCase):
    
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine)

        self.office = Office(name='office', phone='1234567', sales_num=10)
        session.add(self.office)
        session.commit() 

        self.agent = Agent(name='agent', email='agent@gmail.com', office_id=self.office.id)
        session.add(self.agent)
        session.commit() 

        self.buyer = Buyer(name='buyer',  email='buyer@gmail.com')
        session.add(self.buyer)
        session.commit()

        self.house = House(bedrooms=4, bathrooms=3, price=500000, zipcode=67890, date_listing=date.today(), sold=True)
        session.add(self.house)
        session.commit()

    def tearDown(self):
        session.rollback()

    def test_sales_create(self):
        
        sales = Sales(house_id=self.house.id, buyer_id=self.buyer.id, agent_id=self.agent.id, price=self.house.price, date_listing=date.today(), date_sold=date.today(), office_id=self.office.id)
        session.add(sales)
        session.commit()


        self.assertEqual(sales.house_id, self.house.id)
        self.assertEqual(sales.buyer_id, self.buyer.id)
        self.assertEqual(sales.agent_id, self.agent.id)
        self.assertEqual(sales.price, self.house.price)
        self.assertEqual(sales.date_listing, date.today())
        self.assertEqual(sales.date_sold, date.today())
        self.assertEqual(sales.office_id, self.office.id)

    def test_sales_represantation(self):
        sales = Sales(house_id=self.house.id, buyer_id=self.buyer.id, agent_id=self.agent.id, price=self.house.price, date_listing=date.today(), date_sold=date.today(), office_id=self.office.id)

        self.assertEqual(str(sales), "<Sales(id=None, house_id={}, buyer_id={}, agent_id={}, price={}, date_listing={}, date_sold={}, office_id={})>".format(self.house.id, self.buyer.id, self.agent.id, self.house.price, date.today().strftime('%Y-%m-%d'), date.today().strftime('%Y-%m-%d'), self.office.id))

if __name__ == '__main__':
    unittest.main()
