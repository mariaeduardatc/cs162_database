from sqlalchemy import Index, desc, func
from extensions import session


from databases.agent_db import Agent
from databases.comissions_db import Comissions
from databases.house_db import House
from databases.office_db import Office
from databases.sales_db import Sales

# Create an index on the date_created column of the Sales table
# This will speed up queries that filter on this column
Sales.__table__.indexes.add(Index('idx_sales_date_created', Sales.date_sold))

def top5_offices(beg_month, end_month):
    """
        Returns a list of the top 5 offices with the highest number of sales during the specified period.

        Parameters
        --------------
            - beg_month (datetime.datetime): The start of the period (inclusive). Only sales with a creation date
                greater than or equal to this value will be considered.
            - end_month (datetime.datetime): The end of the period (inclusive). Only sales with a creation date
                less than or equal to this value will be considered.

        Returns
        --------------
            - list: A list of 5 tuples, each containing an Office object and the number of sales it had during the
                specified period, sorted in descending order by the number of sales.
    """

    top5_offices = (
        session.query(Sales.id, Office.name, func.count(Office.id))
        .join(Agent, Sales.agent_id == Agent.id)
        .join(Office, Agent.office_id == Office.id)
        .filter(
            Sales.date_sold >= beg_month,
            Sales.date_sold <= end_month,
        )
        .group_by(Office.id)
        .order_by(desc(func.count(Office.id)))
        .limit(5)
        .all()
    )
    return top5_offices

def top5_agents(beg_month, end_month):
    """
        Returns a list of the top 5 agents with the highest number of sales during the specified period.

        Parameters
        --------------
            - beg_month (datetime.datetime): The start of the period (inclusive). Only sales with a creation date
                greater than or equal to this value will be considered.
            - end_month (datetime.datetime): The end of the period (inclusive). Only sales with a creation date
                less than or equal to this value will be considered.

        Returns
        --------------
            - list: A list of 5 tuples, each containing an Agent object and the number of sales they had during the
                specified period, sorted in descending order by the number of sales.
    """
    top5_agents = (
        session.query(Agent.name, func.count(Agent.id))
        .join(Sales, Agent.id == Sales.agent_id)
        .filter(
            Sales.date_sold >= beg_month,
            Sales.date_sold <= end_month,
        )
        .group_by(Agent.id)
        .order_by(desc(func.count(Agent.id)))
        .limit(5)
        .all()
    )
    return top5_agents


# indexing, similar to the Sales case
House.__table__.indexes.add(Index('idx_house_date_created', House.date_listing))


def avg_selling_price(beg_month, end_month):
    """
        Calculates the average selling price of all houses sold within a specified time period.

        Parameters
        --------------
            - beg_month (datetime.datetime): The start of the period (inclusive). Only houses sold with a creation date
                greater than or equal to this value will be considered.
            - end_month (datetime.datetime): The end of the period (inclusive). Only houses sold with a creation date
                less than or equal to this value will be considered.

        Returns
        --------------
            - float: The average selling price of all houses sold within the specified time period, rounded to 2 decimal
                places. If there are no houses sold within the specified time period, returns None.
    """
    avg_selling = (
        session.query(
            func.round(func.avg(House.price), 2)
        )
        .filter(
            House.sold == True,
            House.date_listing >= beg_month,
            House.date_listing <= end_month
        )
        .limit(1)
        .all()
    )
    return avg_selling

def avg_days_market(beg_month, end_month):
    """
        Calculates the average number of days that a house was on the market before being sold during the specified period.

    Parameters
    --------------
        - beg_month (datetime.datetime): The start of the period (inclusive). Only houses with a creation date
            greater than or equal to this value will be considered.
        - end_month (datetime.datetime): The end of the period (inclusive). Only houses with a creation date
            less than or equal to this value will be considered.

    Returns
    --------------
        - list: A list containing a single tuple, containing the average number of days that a house was on the market
            during the specified period, rounded to the nearest whole number.

    """
    avg_days = (
        session.query(
            func.round(
                func.avg(
                    func.julianday(Sales.date_sold)
                    - func.julianday(Sales.date_listing)
                )
            )
        )
        .join(House,Sales.house_id == House.id )
        .filter(
            House.sold == True,
            House.date_listing >= beg_month,
            House.date_listing <= end_month
        )
        .limit(1)
        .all()
    )
    return avg_days

def commission_calc(beg_month, end_month):
    """
        Calculates the commission for each agent based on their sales during a specified period.

        Extra explanation: This function retrieves all sales made by agents within the specified period and their corresponding sale prices.
        Then, it calculates the commission earned by each agent based on the commission rate assigned to the sale price range
        in which the sale falls. The commission earned is stored in the Comissions table in the database, along with the
        corresponding agent and month of the commission.

        Parameters
        --------------
            - beg_month (datetime.datetime): The start of the period (inclusive). Only sales with a creation date
                greater than or equal to this value will be considered.
            - end_month (datetime.datetime): The end of the period (inclusive). Only sales with a creation date
                less than or equal to this value will be considered.

        Returns
        --------------
            - None
    """

    # transaction
    # Get all orders for the given month, and their corresponding agents and prices.
    sales_num = (
        session.query(Agent, House.price)
        .join(Sales, Agent.id == Sales.agent_id)
        .join(House, Sales.house_id == House.id)
        .filter(
            Sales.date_sold >= beg_month,
            Sales.date_sold <= end_month,
        )
        .order_by(Agent.id)
        .all()
    )
    
    for sale in sales_num:
        sale_price = sale[1]
        sale_agent = sale[0]

        if sale_price <= 100000:
            comission = sale_price*0.1
        elif 100000 < sale_price <= 200000:
            comission = sale_price*0.075
        elif 200000 < sale_price <= 500000:
            comission = sale_price*0.06
        elif 500000 < sale_price <= 1000000:
            comission = sale_price*0.05
        else:
            comission = sale_price*0.04
        
        comission_db = Comissions(agent_id = sale_agent.id, comission = comission, month = end_month)

        session.add(comission_db)
        session.commit()
