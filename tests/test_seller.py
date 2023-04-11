import unittest

from databases.seller_db import Seller

from extensions import Base
from tests.tests_extensions import session, engine


class TestSeller(unittest.TestCase):
    """
        Methods
        -------
            setUp():
                Drops all tables, creates tables and rolls back the session.
            tearDown():
                Roll back the session.
            test_create_seller():
                Test creating a Seller instance and verify that the values are correct.
            test_seller_repr():
                Test that the string representation of a Seller instance is as expected.

        Attributes
        ----------
            N/A
    """
    def setUp(self):
        """
            Method that drops all tables, creates tables and rolls back the session.
        """
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

    def tearDown(self):
        """
            Method that rolls back the session.
        """
        session.rollback()

    def test_create_seller(self):
        """
            Test creating a Seller instance and verify that the values are correct.
        """
        seller = Seller(name='seller', phone='555-1234')
        session.add(seller)
        session.commit()

        self.assertIsNotNone(seller.id)
        self.assertEqual(seller.name, 'seller')
        self.assertEqual(seller.phone, '555-1234')

    def test_seller_repr(self):
        """
            Test the representation of a Seller instance as a string.
        """
        seller = Seller(name='seller', phone='555-1234')
        self.assertEqual(str(seller), "<Seller(id=None, name=seller, phone=555-1234)>")

if __name__ == '__main__':
    unittest.main()