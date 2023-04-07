from sqlalchemy import Date, Column,  Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from databases.agent_db import Agent
from databases.house_db import House
from databases.buyer_db import Buyer


Base = declarative_base() 


# creating the Agent db
class Sales(Base):
	__tablename__ = 'sales'
	id = Column(Integer, primary_key = True)
	house_id = Column(Integer, ForeignKey={'house.id'})
	buyer_id = Column(Integer, ForeignKey={'buyer.id'})
	agent_id = Column(Integer, ForeignKey={'agent.id'})
	price = Column(Integer, ForeignKey={'house.price'})
	date = Column(Date)
	
    # GATHER INFO ON COMISSION AND CHANGE HOUSE STATUS IG IT DOES NOT HAPPEN HERE

	house = relationship(House)
	buyer = relationship(Buyer)
	agent = relationship(Agent)


	def __repr__(self):
		return "<Sales(id={0}, house_id={1}, buyer_id={2}, agent_id={3}, price={4}, date={6})>".format(self.id, self.house_id, self.buyer_id, self.agent_id, self.price, self.date)