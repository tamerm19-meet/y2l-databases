from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class CC(Base):
   __tablename__ = 'CC'
   cc_number = Column(Integer, primary_key=True)
   wacky_numbers = Column(Integer)
   expiration_date = Column(Integer)
   tamer2 = Column(String)
   tamer = Column(String)

