from sqlalchemy import Date, Column, ForeignKey,  Integer

from extensions import Base

# creating the Agent db
class Sales(Base):
	"""
	    Represents the sales table in the database.

	Attributes
	--------------
        - id (int): The primary key of the table.
        - house_id (int): The foreign key referencing the id of a house in the houses table.
        - buyer_id (int): The foreign key referencing the id of a buyer in the buyers table.
        - agent_id (int): The foreign key referencing the id of an agent in the agents table.
        - price (int): The price of the house.
        - date_listing (date): The date the house was listed.
        - date_sold (date): The date the house was sold.
        - office_id (int): The foreign key referencing the id of an office in the offices table.

	Methods
	-----------
        __repr__()
            Returns a string representation of the instance.
	"""
	# data normalization -> columns are directly connected to the id
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
		return "<Sales(id={0}, house_id={1}, buyer_id={2}, agent_id={3}, price={4}, date_listing={5}, date_sold={6}, office_id={7})>".format(self.id, self.house_id, self.buyer_id, self.agent_id, self.price, self.date_listing, self.date_sold, self.office_id)