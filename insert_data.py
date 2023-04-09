from databases.house_db import House
from databases.office_db import Office
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