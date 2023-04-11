import unittest
from extensions import Base
from tests.tests_configuration import TestConfig
from tests.tests_extensions import session, engine
from databases.buyer_db import Buyer

class TestBuyer(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

    def tearDown(self):
        session.rollback()

    def test_buyer_creation(self):
        buyer = Buyer(name='John Doe', email='johndoe@example.com')
        session.add(buyer)
        session.commit()

        self.assertIsNotNone(buyer.id)
        self.assertEqual(buyer.name, 'John Doe')
        self.assertEqual(buyer.email, 'johndoe@example.com')

    def test_buyer_representation(self):
        buyer = Buyer(name='John Doe', email='johndoe@example.com')
        self.assertEqual(str(buyer), "<Buyer(id=None, name=John Doe, email=johndoe@example.com)>")

if __name__ == '__main__':
    unittest.main()
