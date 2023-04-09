from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from databases.agent_db import Agent

	
# to create the db
engine = create_engine('sqlite:///agent.db')
engine.connect()  

Base = declarative_base() 

# creating the Seller db
class Comissions(Base):
	__tablename__ = 'comissions'
	id = Column(Integer, primary_key = True)
	agent_id = Column(Integer, ForeignKey('agent.id'))
	comission = Column(Float)
	month =  Column(DateTime)

	agent = relationship(Agent)
	
	def __repr__(self):
		return "<Comissions(id={0}, agent_id={1}, comission={2})>".format(self.id, self.agent_id, self.comission)
