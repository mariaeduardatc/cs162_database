from sqlalchemy import Boolean, Date, Column, ForeignKey, Integer, String 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base() 

# creating the House db
class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    price = Column(Integer)
    zipcode = Column(Integer)
    date_listing = Column(Date)
    sold = Column(Boolean)
    seller_id = Column(Integer, ForeignKey('seller.id'))

    sellers = relationship('Seller', back_populates='house')

    
    def __repr__(self):
        return "<House(id={0}, bedrooms={1}, bathrooms={2}, price={3}, zipcode={4}, date_listing={5}, sold={6}, seller_id={7})>".format(self.id, self.bedrooms, self.bathrooms, self.price, self.zipcode, self.date_listing, self.sold, self.seller_id)
