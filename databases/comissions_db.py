from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


# to create the db
engine = create_engine('sqlite:///comissions.db')
Base = declarative_base()
Base.metadata.create_all(engine)

# creating the Comissions db
class Comissions(Base):
    __tablename__ = 'comissions'
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey('agent.id'))
    comission = Column(Float)
    month = Column(DateTime)

    agents = relationship('Agent', back_populates='comissions')

    def __repr__(self):
        return "<Comissions(id={0}, agent_id={1}, comission={2}, month={3})>".format(self.id, self.agent_id, self.comission, self.month)

