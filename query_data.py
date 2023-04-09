from sqlalchemy import desc, func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base


from databases.agent_db import Agent
from databases.comissions_db import Comissions
from databases.house_db import House
from databases.office_db import Office
from databases.sales_db import Sales


def top5_offices(beg_month, end_month):

    top5_offices = (
        Office.query(func.count(Office.id))
        .join(Sales, Office.id == Sales.office_id)
        .filter(
            Sales.date_created >= beg_month,
            Sales.date_created <= end_month,
        )
        .group_by(Office.id)
        .order_by(desc(func.count(Office.id)))
        .limit(5)
        .all()
    )
    return top5_offices

def top5_agents(beg_month, end_month):
    top5_agents = (
        Agent.query(func.count(Agent.id))
        .join(Sales, Agent.id == Sales.agent_id)
        .filter(
            Sales.date_created >= beg_month,
            Sales.date_created <= end_month,
        )
        .group_by(Agent.id)
        .order_by(desc(func.count(Agent.id)))
        .limit(5)
        .all()
    )
    return top5_agents


def avg_selling_price(beg_month, end_month):
    avg_selling = (
        House.query(
            func.round(func.avg(House.price), 2)
        )
        .filter(
            House.sold == True,
            House.date_created >= beg_month,
            House.date_created <= end_month
        )
        .limit(1)
        .all()
    )
    return avg_selling

def avg_days_market(beg_month, end_month):
    avg_days = (
        House.query(
            func.round(
                func.avg(
                    func.julianday(House.date_sold)
                    - func.julianday(House.date_created)
                )
            )
        )
        .filter(
            House.sold == True,
            House.date_created >= beg_month,
            House.date_created <= end_month
        )
        .limit(1)
        .all()
    )
    return avg_days

def commission_calc(beg_month, end_month):

    # Get all orders for the given month, and their corresponding agents and prices.
    sales_num = (
        session.query(Agent, House.price)
        .join(Sales, Agent.id == Sales.agent_id)
        .join(House, Sales.listing_id == House.id)
        .filter(
            Sales.date_created >= beg_month,
            Sales.date_created <= end_month,
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
        
        comission_db = Comissions(agent_id = sale_agent, comission = comission, month = end_month)

        # to create the db
        engine = create_engine('sqlite:///comissions.db')
        engine.connect() 

        Base = declarative_base() 

        Base.metadata.create_all(bind=engine) 

        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(comission_db)
        session.commit()