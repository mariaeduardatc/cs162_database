from sqlalchemy import Column, Float, ForeignKey, Integer, create_engine
from sqlalchemy.orm import sessionmaker 
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

	agent = relationship(Agent)
	
	def __repr__(self):
		return "<Comissions(id={0}, agent_id={1}, comission={2})>".format(self.id, self.agent_id, self.comission)

Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()