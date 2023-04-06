from sqlalchemy import Date, Numeric, create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy.dialects.mysql import VARCHAR

from databases.seller_db import Seller

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
	status = Column(VARCHAR(11)) # "SOLD" or "SELLING"
	seller_id = Column(Integer, ForeignKey=('seller.id'))

	seller = relationship(Seller)
	

    # CHANGE THIS LATER
	def __repr__(self):
		return "<House(id={0}, bedrooms={1}, email={2}, phone={3})>".format(self.id, self.name, self.email, self.phone)
	

Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()