from requests import session
from databases.comissions_db import Comissions
from databases.house_db import House
from databases.sales_db import Sales

from faker.agent_faker import create_agent
from faker.buyer_faker import create_buyer
from faker.house_faker import create_house
from faker.office_faker import create_office
from faker.sales_faker import create_sales
from faker.seller_faker import create_seller

# variables
buyers_num = 500
house_num = buyers_num//3
office_num = house_num//5
agents_num = office_num * 4
seller_num = house_num
sales_num = house_num//3


# creating the fake data
create_agent(agents_num, office_num)
create_buyer(buyers_num)
create_house(house_num, agents_num)
create_office(office_num)
create_sales(sales_num, house_num, buyers_num, agents_num)
create_seller(seller_num)


# populating the comissions' db
for sale in sales_num:
    id_agent = session.query(Sales).filter_by(id=sale.id).first().agent_id
    sale_price = session.query(Sales).filter_by(id=sale.id).first().price

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
    
    comission_db = Comissions(agent_id = id_agent, comission = comission)
    
    session.add(comission_db)
    session.commit()

    # changing status of house
    id_house = session.query(Sales).filter_by(id=sale.id).first().house_id

    change_status = session.query(House).filter_by(id=id_house).status