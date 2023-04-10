from sqlalchemy import Column, Text, Integer

from extensions import Base



# creating the Buyer db
class Buyer(Base):
	__tablename__ = 'buyer'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	email = Column(Text)

	def __repr__(self):
		return "<Buyer(id={0}, name={1}, email={2})>".format(self.id, self.name, self.email)