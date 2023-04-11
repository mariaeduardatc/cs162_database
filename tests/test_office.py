import unittest
from extensions import Base, engine, session
from databases.office_db import Office


class TestOffice(unittest.TestCase):
    """
        A unittest class for testing the Office model.

    Methods
    -------
        setUp():
            Drops all tables, creates tables and rolls back the session.
        tearDown():
            Roll back the session.
        test_office_creation():
            Test creating a Office instance and verify that the values are correct.

    Attributes
    ----------
        N/A
    """
    
    def setUp(self):
        """
            Method called to prepare the test fixture.
        """
        self.tearDown()
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        """
            Method called after each test case to rollback the session and clean up.
        """
        session.rollback()

    def test_office_create(self):
        """
            Test case to check if a new office can be created.
        """
        office = Office(name='Office1', phone='1234567', sales_num=10)
        session.add(office)
        session.commit()

        self.assertEqual(office.name, 'Office1')
        self.assertEqual(office.phone, '1234567')
        self.assertEqual(office.sales_num, 10)

    def test_office_representation(self):
        """
            Test case to check the string representation of the Office object.
        """
        office = Office(name='Office2', phone='7654321', sales_num=5)

        self.assertEqual(str(office), "<Office(id=None, name=Office2, phone=7654321, sales_num5)>")

if __name__ == '__main__':
    unittest.main()
