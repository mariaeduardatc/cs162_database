import unittest
from datetime import date
from databases.house_db import House
from databases.seller_db import Seller
from extensions import Base
from tests.tests_extensions import session, engine

class TestHouse(unittest.TestCase):
    
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine)

        self.seller = Seller(name='seller', phone='9876453')
        session.add(self.seller)
        session.commit() 

    def tearDown(self):
        session.rollback()

    def test_house_create(self):
        
        house = House(bedrooms=4, bathrooms=3, price=500000, zipcode=67890, date_listing=date.today(), sold=True, seller_id=self.seller.id)
        print(self.seller.id, "TEST", )
        session.add(house)
        session.commit()

        self.assertEqual(house.bedrooms, 4)
        self.assertEqual(house.bathrooms, 3)
        self.assertEqual(house.price, 500000)
        self.assertEqual(house.zipcode, 67890)
        self.assertEqual(house.date_listing, date.today())
        self.assertEqual(house.sold, True)
        self.assertEqual(house.seller_id, self.seller.id)
        

    def test_house_represantation(self):
        house = House(bedrooms=3, bathrooms=2, price=250000, zipcode=12345, date_listing=date.today(), sold=False, seller_id=self.seller.id)

        self.assertEqual(str(house), "<House(id=None, bedrooms=3, bathrooms=2, price=250000, zipcode=12345, date_listing={}, sold=False, seller_id={})>".format(date.today(), self.seller.id))
        
if __name__ == '__main__':
    unittest.main()
