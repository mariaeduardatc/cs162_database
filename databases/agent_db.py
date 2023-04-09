from sqlalchemy import Column, ForeignKey, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base() 


# creating the Agent db
class Agent(Base):
	__tablename__ = 'agent'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	email = Column(Text)
	sales = Column(Integer)
	office_id = Column(Integer, ForeignKey('office.id'))

	offices = relationship('Office', back_populates='agent')
	comissions = relationship('Comissions', back_populates='agent')


	def __repr__(self):
		return "<Agent(id={0}, name={1},  email={2}, sales={3}, office_id={4})>".format(self.id, self.name, self.email, self.sales, self.office_id)
	