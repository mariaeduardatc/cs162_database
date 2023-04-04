import sqlalchemy 
from sqlalchemy import Date, Numeric, create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy.dialects.mysql import VARCHAR

# to create the db
engine = create_engine('sqlite:///seller.db')
engine.connect() 

Base = declarative_base() 


# creating the Seller db
class Seller(Base):
	__tablename__ = 'seller'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	email = Column(Text)
	phone = Column(Integer)

	def __repr__(self):
		return "<Seller(id={0}, name={1}, email={2}, phone={3})>".format(self.id, self.name, self.email, self.phone)