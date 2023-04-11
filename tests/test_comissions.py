from datetime import datetime
import unittest

from databases.agent_db import Agent
from databases.comissions_db import Comissions
from extensions import Base
from tests.tests_extensions import session, engine


class TestComissions(unittest.TestCase):
    """
    This class contains the unit tests for the Comissions class.

    Methods
    ---------
        setUp(self):
            Initializes the test case by creating a new database and adding a new agent to the database.
        
        tearDown(self):
            Rolls back the database changes made during the test case.

        test_create_comission(self):
            Tests if a new comission can be created and added to the database.
        
        test_comission_representation(self):
            Tests if the string representation of a comission object is correct.

    """
    def setUp(self):
        """
            Initializes the test case by creating a new database and adding a new agent to the database.
        """
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

        self.agent = Agent(name='agent', email='agent@example.com', sales=1, office_id=1)
        session.add(self.agent)
        session.commit()

    def tearDown(self):
        """
            Roll back the current transaction, undoing any changes made during the test.
        """
        session.rollback()

    def test_create_comission(self):
        """
        Tests if a new comission can be created and added to the database.

        Asserts:
            - comission object has been assigned an id.
            - agent_id of the comission object is correct.
            - comission amount of the comission object is correct.
            - month of the comission object is correct.
        """
        comission = Comissions(agent_id=self.agent.id, comission=10.5, month=datetime(2023, 3, 1))
        session.add(comission)
        session.commit()

        self.assertIsNotNone(comission.id)
        self.assertEqual(comission.agent_id, self.agent.id)
        self.assertEqual(comission.comission, 10.5)
        self.assertEqual(comission.month, datetime(2023, 3, 1))

    def test_comission_representation(self):
        """
        Tests if the string representation of a comission object is correct.

        Asserts:
            - The string representation of the comission object is equal to the expected string representation.
        """
        comission = Comissions(agent_id=self.agent.id, comission=10.5, month=datetime(2023, 3, 1))
        self.assertEqual(str(comission), "<Comissions(id=None, agent_id={}, comission=10.5, month=2023-03-01 00:00:00)>".format(self.agent.id))
