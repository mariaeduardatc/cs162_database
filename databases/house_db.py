from sqlalchemy import Date, Numeric, create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy.dialects.mysql import VARCHAR

# to create the db
engine = create_engine('sqlite:///house.db')
engine.connect() 

Base = declarative_base() 


# creating the House db
class House(Base):
	__tablename__ = 'house'
	id = Column(Integer, primary_key = True)
	bedrooms = Column(Integer)
	bathrooms = Column(Integer)
	# FIND A BETTER TYPE HERE:
	price = Column(Integer)
	zipcode = Column(Integer)
	date_listing = Column(Date)
	status = Column(Text) # "SOLD" or "SELLING"

    # CHANGE THIS LATER
	def __repr__(self):
		return "<House(id={0}, bedrooms={1}, email={2}, phone={3})>".format(self.id, self.name, self.email, self.phone)