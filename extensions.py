from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.ext.declarative import declarative_base

# creates instance which manages the connection to the database
# type of database (sqlite) + name (app)
engine = create_engine('sqlite:///app.db')

# creates a connection to the database using the engine instance created 
engine.connect()

# creates a base class for declarative class definitions
Base = declarative_base()
Session = sessionmaker(bind=engine)

# used to interact with the database
session = Session()