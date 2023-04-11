from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from tests.tests_configuration import TestConfig

# Initializing db on SQLAlchemy
engine = create_engine(TestConfig.SQLALCHEMY_DATABASE_URI)
engine.connect()


Session = sessionmaker(bind=engine)
session = Session()
