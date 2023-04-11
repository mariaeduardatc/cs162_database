import unittest
from extensions import Base, engine, session
from databases.office_db import Office


class TestOffice(unittest.TestCase):
    
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        session.rollback()

    def test_office_create(self):
        office = Office(name='Office1', phone='1234567', sales_num=10)
        session.add(office)
        session.commit()

        self.assertEqual(office.name, 'Office1')
        self.assertEqual(office.phone, '1234567')
        self.assertEqual(office.sales_num, 10)

    def test_office_representation(self):
        office = Office(name='Office2', phone='7654321', sales_num=5)

        self.assertEqual(str(office), "<Office(id=None, name=Office2, phone=7654321, sales_num5)>")

if __name__ == '__main__':
    unittest.main()
