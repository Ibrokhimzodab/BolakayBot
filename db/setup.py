from sqlalchemy import create_engine, Column, MetaData, Integer, String, Boolean, BigInteger, JSON, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Create the engine and session

import os

try:
    engine = create_engine("postgresql://postgres:postgres@localhost:5432/bolakay?client_encoding=utf8")
except Exception as error:
    print("Error while connecting to PostgreSQL:", error)

Session = sessionmaker(bind=engine)
session = Session()
query = session.query

# Create a base class for declarative models
Base = declarative_base()




