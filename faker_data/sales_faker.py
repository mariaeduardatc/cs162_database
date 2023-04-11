import datetime
import random
from faker import Faker

from extensions import session
from databases.house_db import House
from databases.sales_db import Sales

def create_sales(sales_num, house_num, buyers_num, agents_num):
    """
        Creates a specified number of Sales instances with randomized data and saves them to the database.
        Also, changes the status of the sold house.
    
    Parameters
    ----------
        - sales_num (int) : The number of sales to create.
        - house_num (int) : The number of houses available for selling.
        - buyers_num (int) : The number of buyers available for making purchases.
        - agents_num (int) : The number of agents available for handling sales.

    Returns
    -------
        None
    """
    for i in range(sales_num):
        fake = Faker()
        
        house_id = random.choice([i + 1 for i in range(house_num)])
        house_query = session.query(House).filter_by(id=house_id).first()

        house_price = house_query.price
        date_sold = house_query.date_listing + datetime.timedelta(
                days=random.randint(5, 50)
            )
        sales = Sales(**{
            "house_id": house_id,
            "buyer_id": random.choice([i + 1 for i in range(buyers_num)]),
            "agent_id": random.choice([i + 1 for i in range(agents_num)]),
            "price":  house_price,
            "date_listing": house_query.date_listing,
            "date_sold": date_sold
            })
        
        session.add(sales)
        
        # transaction
        # changing status of the sold house
        house_sold = session.query(House).filter_by(id=house_id).first()
        house_sold.date_sold = date_sold
        house_sold.sold = True
    session.commit()
