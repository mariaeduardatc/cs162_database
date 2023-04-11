import unittest
from extensions import Base
from tests.tests_configuration import TestConfig
from tests.tests_extensions import session, engine
from databases.buyer_db import Buyer

class TestBuyer(unittest.TestCase):
    """
        A class for testing Buyer database model.

    Methods
    -------
        setUp():
            Drops all tables, creates tables and rolls back the session.
        tearDown():
            Roll back the session.
        test_buyer_creation():
            Test creating a Buyer instance and verify that the values are correct.

    Attributes
    ----------
        N/A
    """
    def setUp(self):
        """
            Set up the test case by dropping all the tables in the database and creating new tables based on the metadata.
        """
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

    def tearDown(self):
        """
            Roll back the current transaction, undoing any changes made during the test.
        """
        session.rollback()

    def test_buyer_creation(self):
        """
            Test the creation of a Buyer object.

            - Create a new Buyer object.
            - Add it to the session.
            - Commit the session.
            - Check that the Buyer object has an ID and its attributes are correct.
        """
        buyer = Buyer(name='John Doe', email='johndoe@example.com')
        session.add(buyer)
        session.commit()

        self.assertIsNotNone(buyer.id)
        self.assertEqual(buyer.name, 'John Doe')
        self.assertEqual(buyer.email, 'johndoe@example.com')

    def test_buyer_representation(self):
        """
            Test the string representation of a Buyer object.

            - Create a new Buyer object.
            - Check that the string representation of the Buyer object is correct.
        """
        buyer = Buyer(name='John Doe', email='johndoe@example.com')
        self.assertEqual(str(buyer), "<Buyer(id=None, name=John Doe, email=johndoe@example.com)>")

if __name__ == '__main__':
    unittest.main()
