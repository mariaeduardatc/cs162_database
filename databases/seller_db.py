from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
# to create the db
 

Base = declarative_base() 


# creating the Seller db
class Seller(Base):
	__tablename__ = 'seller'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Integer)

	def __repr__(self):
		return "<Seller(id={0}, name={1}, phone={2})>".format(self.id, self.name, self.phone)