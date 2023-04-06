from sqlalchemy import create_engine, Column, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker 
# to create the db
engine = create_engine('sqlite:///seller.db')
engine.connect() 

Base = declarative_base() 


# creating the Seller db
class Seller(Base):
	__tablename__ = 'seller'
	id = Column(Integer, primary_key = True)
	name = Column(Text)
	phone = Column(Integer)

	def __repr__(self):
		return "<Seller(id={0}, name={1}, phone={2})>".format(self.id, self.name, self.phone)
	
Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()


seller_1 = Seller(id = 1, name = "John Cena", phone = 67548392)
seller_2 = Seller(id = 2, name = "Patricia Kane", phone = 98548392)
seller_3 = Seller(id = 3, name = "Ana Silva", phone = 98654630)
seller_4 = Seller(id = 4, name = "Rick Morty", phone = 98999630)
seller_5 = Seller(id = 5, name = "Sofia Post", phone = 97654362)


sellers = [seller_1, seller_2, seller_3, seller_4, seller_5]

for seller in sellers:
	session.add(seller)
	session.commit()

print(session.query(Seller).all())
