from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from extensions import Base


# creating the Comissions db
class Comissions(Base):
    """
        Represents the commissions table in the database.

    Attributes
    --------------
        - id (int): The primary key of the table.
        - agent_id (int): The foreign key referencing the id of an agent in the agents table.
        - comission (float): The amount of commission earned.
        - month (datetime): The month in which the commission was earned.

    Methods
    -----------
        __repr__()
            Returns a string representation of the instance.
    """
    __tablename__ = 'comissions'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agent.id'))
    comission = Column(Float)
    month = Column(DateTime)

    def __repr__(self):
        return "<Comissions(id={0}, agent_id={1}, comission={2}, month={3})>".format(self.id, self.agent_id, self.comission, self.month)

