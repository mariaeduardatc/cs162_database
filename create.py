from extensions import Base

from databases.comissions_db import Comissions
from databases.office_db import Office
from databases.buyer_db import Buyer
from databases.house_db import House
from databases.sales_db import Sales
from databases.seller_db import Seller
from databases.agent_db import Agent

from extensions import engine



Base.metadata.drop_all(bind=engine) 
Base.metadata.create_all(bind=engine) 