from sqlalchemy import Column, Text, Integer

from extensions import Base



# creating the Buyer db
class Buyer(Base):
	"""
		Represents a buyer in the database.

	Attributes
	--------------
			- id (int): The unique identifier for the buyer.
			- name (str): The name of the buyer.
			- email (str): The email address of the buyer.
			
	Methods:
	-----------
        __repr__()
            Returns a string representation of the instance.
	"""
	# data normalization -> columns are directly connected to the id
	__tablename__ = 'buyer'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	email = Column(Text)

	def __repr__(self):
		return "<Buyer(id={0}, name={1}, email={2})>".format(self.id, self.name, self.email)