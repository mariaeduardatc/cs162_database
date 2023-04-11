from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from extensions import Base


# creating the Agent db
class Office(Base):
	__tablename__ = 'office'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Text)
	sales_num = Column(Integer)
	agents = relationship('Agent', backref='post')


	def __repr__(self):
		return "<Office(id={0}, name={1}, phone={2}, sales_num{3})>".format(self.id, self.name, self.phone, self.sales_num)