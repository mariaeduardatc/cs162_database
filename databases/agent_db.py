from sqlalchemy import Column, ForeignKey, Text, Integer
from sqlalchemy.orm import relationship
from extensions import Base

from databases.comissions_db import Comissions

# creating the Agent db
class Agent(Base):
	"""
		Represents a real estate agent in the database.

	Attributes
	----------------
		- id (int): The unique identifier for the agent.
		- name (str): The name of the agent.
		- email (str): The email address of the agent.
		- sales (int): The number of sales made by the agent.
		- office_id (int): The ID of the office where the agent works.
		- comissions (list of Comissions): A list of comissions earned by the agent.

	Methods
        -----------
        __repr__()
            Returns a string representation of the instance.

	"""
	__tablename__ = 'agent'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	email = Column(Text)
	sales = Column(Integer)
	office_id = Column(Integer, ForeignKey('office.id'))
	comissions = relationship('Comissions', backref='post')


	def __repr__(self):
		return "<Agent(id={0}, name={1},  email={2}, sales={3}, office_id={4})>".format(self.id, self.name, self.email, self.sales, self.office_id)
	