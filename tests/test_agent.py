import unittest

from databases.agent_db import Agent
from databases.office_db import Office
from extensions import Base
from tests.tests_extensions import session, engine


class TestAgent(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

    def tearDown(self):
        session.rollback()

    def test_agent_creation(self):
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
