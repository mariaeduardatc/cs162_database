from extensions import Base
from databases.agent_db import Agent
from databases.buyer_db import Buyer
from databases.house_db import House
from databases.office_db import Office
from databases.sales_db import Sales
from databases.seller_db import Seller

from extensions import engine



Base.metadata.create_all(bind=engine) 