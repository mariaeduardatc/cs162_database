from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from extensions import Base

# creating the Seller db
class Seller(Base):
	"""
	    Represents the sellers table in the database.

	Attributes
	--------------
        - id (int): The primary key of the table.
        - name (str): The name of the seller.
        - phone (str): The phone number of the seller.

	Methods
	-----------
        __repr__()
            Returns a string representation of the instance.
	"""
	# data normalization -> columns are directly connected to the id
	__tablename__ = 'seller'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Text)

	def __repr__(self):
		return "<Seller(id={0}, name={1}, phone={2})>".format(self.id, self.name, self.phone)