from datetime import datetime
import unittest

from databases.agent_db import Agent
from databases.comissions_db import Comissions
from extensions import Base
from tests.tests_extensions import session, engine


class TestComissions(unittest.TestCase):
    def setUp(self):
        self.tearDown()
        Base.metadata.create_all(bind=engine) 

        self.agent = Agent(name='agent', email='agent@example.com', sales=1, office_id=1)
        session.add(self.agent)
        session.commit()

    def tearDown(self):
        session.rollback()

    def test_create_comission(self):
        comission = Comissions(agent_id=self.agent.id, comission=10.5, month=datetime(2023, 3, 1))
        session.add(comission)
        session.commit()

        self.assertIsNotNone(comission.id)
        self.assertEqual(comission.agent_id, self.agent.id)
        self.assertEqual(comission.comission, 10.5)
        self.assertEqual(comission.month, datetime(2023, 3, 1))

    def test_comission_representation(self):
        comission = Comissions(agent_id=self.agent.id, comission=10.5, month=datetime(2023, 3, 1))
        self.assertEqual(str(comission), "<Comissions(id=None, agent_id={}, comission=10.5, month=2023-03-01 00:00:00)>".format(self.agent.id))
