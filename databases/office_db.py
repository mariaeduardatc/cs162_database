from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base() 


# creating the Agent db
class Office(Base):
	__tablename__ = 'office'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Text)
	sales_num = Column(Integer)

	agents = relationship('Agent', back_populates='office')


	def __repr__(self):
		return "<Office(id={0}, name={1}, phone={2}, sales_num{3})>".format(self.id, self.name, self.phone, self.sales_num)