import unittest
from datetime import date
from databases.house_db import House
from databases.seller_db import Seller
from extensions import Base
from tests.tests_extensions import session, engine

class TestHouse(unittest.TestCase):
    """
        A unittest.TestCase subclass for testing the House model.

    Attributes:
    -----------
        None

    Methods:
    --------
        setUp(self):
            Initializes a new database schema and creates a new Seller object to be used in each test.

        tearDown(self):
            Rolls back any changes made to the database during a test.

        test_house_create(self):
            Tests creating a new House object and checking if its attributes match the ones used in its creation.

        test_house_represantation(self):
            Tests if the string representation of a House object is correctly formatted.
    """
    
    def setUp(self):
        """
            Initializes a new database schema and creates a new Seller object to be used in each test.
        """
        self.tearDown()
        Base.metadata.create_all(bind=engine)

        self.seller = Seller(name='seller', phone='9876453')
        session.add(self.seller)
        session.commit() 

    def tearDown(self):
        """
            Rolls back any changes made to the database during a test.
        """
        session.rollback()

    def test_house_create(self):
        """
            Tests creating a new House object and checking if its attributes match the ones used in its creation.
        """
        
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
        """
            Tests if the string representation of a House object is correctly formatted.
        """
        house = House(bedrooms=3, bathrooms=2, price=250000, zipcode=12345, date_listing=date.today(), sold=False, seller_id=self.seller.id)

        self.assertEqual(str(house), "<House(id=None, bedrooms=3, bathrooms=2, price=250000, zipcode=12345, date_listing={}, sold=False, seller_id={})>".format(date.today(), self.seller.id))
        
if __name__ == '__main__':
    unittest.main()
