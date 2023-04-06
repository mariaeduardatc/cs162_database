from sqlalchemy import Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base() 

# creating the Seller db
class Buyer(Base):
	__tablename__ = 'buyer'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	email = Column(Text)

	def __repr__(self):
		return "<Buyer(id={0}, name={1}, email={2})>".format(self.id, self.name, self.email)


buyer_1 = Buyer(id = 1, name = "Patrick P.", phone = 45628391)
buyer_2 = Buyer(id = 2, name = "Rita S.", phone = 87645298)
buyer_3 = Buyer(id = 3, name = "Lorelay K.", phone = 98762415)
buyer_4 = Buyer(id = 4, name = "Kim K.", phone = 76253748)
buyer_5 = Buyer(id = 5, name = "Alice E.", phone = 98760483)

buyers = [buyer_1, buyer_2, buyer_3, buyer_4, buyer_5]



