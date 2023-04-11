from sqlalchemy import Column, Text, Integer
from sqlalchemy.orm import relationship

from extensions import Base

# creating the Seller db
class Seller(Base):
	__tablename__ = 'seller'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Text)

	# houses = relationship('House', backref='post')

	def __repr__(self):
		return "<Seller(id={0}, name={1}, phone={2})>".format(self.id, self.name, self.phone)