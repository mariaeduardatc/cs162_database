from sqlalchemy import Date, Column, ForeignKey,  Integer
from sqlalchemy.orm import relationship

from extensions import Base

# creating the Agent db
class Sales(Base):
	__tablename__ = 'sales'
	id = Column(Integer, primary_key = True)
	house_id = Column(Integer, ForeignKey('house.id'))
	buyer_id = Column(Integer, ForeignKey('buyer.id'))
	agent_id = Column(Integer, ForeignKey('agent.id'))
	price = Column(Integer, ForeignKey('house.price'))
	date_listing = Column(Date)
	date_sold = Column(Date)
	office_id = Column(Integer, ForeignKey('office.id'))

	def __repr__(self):
		return "<Sales(id={0}, house_id={1}, buyer_id={2}, agent_id={3}, price={4}, date_listing{5}, date_sold={6}, office_id={7})>".format(self.id, self.house_id, self.buyer_id, self.agent_id, self.price, self.date_listing, self.date_sold, self.office_id)