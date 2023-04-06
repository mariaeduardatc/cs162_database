import sqlalchemy 
from sqlalchemy import Date, Numeric, create_engine, Column, Text, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
from sqlalchemy.dialects.mysql import VARCHAR

# to create the db
engine = create_engine('sqlite:///office.db')
engine.connect() 

Base = declarative_base() 


# creating the Agent db
class Office(Base):
	__tablename__ = 'office'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Integer)

	def __repr__(self):
		return "<Office(id={0}, name={1}, phone={2})>".format(self.id, self.name, self.phone)
	
office_1 = Office(id = 1, name = "ABH Estate", phone = 76548392)
office_2 = Office(id = 2, name = "ABH Estate", phone = 76548392)