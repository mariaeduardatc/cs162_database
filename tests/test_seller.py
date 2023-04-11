import unittest

from databases.seller_db import Seller

from extensions import Base
from tests.tests_extensions import session, engine


class TestSeller(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

    def tearDown(self):
        session.rollback()

    def test_create_seller(self):
        seller = Seller(name='seller', phone='555-1234')
        session.add(seller)
        session.commit()

        self.assertIsNotNone(seller.id)
        self.assertEqual(seller.name, 'seller')
        self.assertEqual(seller.phone, '555-1234')

    def test_seller_repr(self):
        seller = Seller(name='seller', phone='555-1234')
        self.assertEqual(str(seller), "<Seller(id=None, name=seller, phone=555-1234)>")

if __name__ == '__main__':
    unittest.main()