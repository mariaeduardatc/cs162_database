from sqlalchemy import Boolean, Date, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from extensions import Base


# creating the House db
class House(Base):
    """
        Represents the House (listings) table in the database.
    Attributes
    --------------
        - id (int): The primary key of the table.
        - bedrooms (int): The number of bedrooms in the house.
        - bathrooms (int): The number of bathrooms in the house.
        - price (int): The price of the house.
        - zipcode (int): The zipcode of the house.
        - date_listing (datetime.date): The date on which the house was listed.
        - sold (bool): A flag indicating whether the house is sold or not.
        - seller_id (int): The foreign key referencing the id of a seller in the sellers table.

    Methods
    -----------
        __repr__()
            Returns a string representation of the instance.
    """
    # data normalization -> columns are directly connected to the id
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    price = Column(Integer)
    zipcode = Column(Integer)
    date_listing = Column(Date)
    sold = Column(Boolean)
    seller_id = Column(Integer, ForeignKey('seller.id'))

    
    def __repr__(self):
        return "<House(id={0}, bedrooms={1}, bathrooms={2}, price={3}, zipcode={4}, date_listing={5}, sold={6}, seller_id={7})>".format(self.id, self.bedrooms, self.bathrooms, self.price, self.zipcode, self.date_listing, self.sold, self.seller_id)
