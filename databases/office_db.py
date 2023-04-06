from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base() 


# creating the Agent db
class Office(Base):
	__tablename__ = 'office'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Integer)

	def __repr__(self):
		return "<Office(id={0}, name={1}, phone={2})>".format(self.id, self.name, self.phone)