import unittest

from databases.agent_db import Agent
from databases.office_db import Office
from extensions import Base
from tests.tests_extensions import session, engine


class TestAgent(unittest.TestCase):
    """
        A class for testing Agent database model.

    Methods
    -------
        setUp():
            Drops all tables, creates tables and rolls back the session.
        tearDown():
            Roll back the session.
        test_agent_creation():
            Test creating an Agent instance and verify that the values are correct.

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

    def test_agent_creation(self):
        """
            Test the creation of an Agent object in the database.
        
            The test creates an office to associate with the agent, then creates an Agent object
            with predefined attributes and adds it to the session. The test asserts that the agent
            was successfully added to the database by checking its ID and comparing its attributes
            with the predefined values.
        """
        # Create an office to associate with the agent
        office = Office(name='Office 1')
        session.add(office)
        session.commit()
        
        agent = Agent(name='agent', email='agent@example.com', sales=1, office_id=office.id)
        session.add(agent)
        session.commit()

        self.assertIsNotNone(agent.id)
        self.assertEqual(agent.name, 'agent')
        self.assertEqual(agent.email, 'agent@example.com')
        self.assertEqual(agent.sales, 1)
        self.assertEqual(agent.office_id, office.id)

if __name__ == '__main__':
    unittest.main()
