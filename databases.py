from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :
def add_cc(cc_number, wacky_numbers, expiration_date, tamer, tamer2):
    """
    Add a student to the database, given
    their name, year, and whether they have
    finished the lab.
    """
    CC_object = CC(
        cc_number=cc_number,
        wacky_numbers=wacky_numbers,
        expiration_date=expiration_date,
        tamer=tamer,
        tamer2=tamer2)
    session.add(CC_object)
    session.commit()

def create_product():

  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def update_product():
  #TODO: complete the functions (you will need to change the function's inputs)
  pass

def delete_product(id):
  pass

def get_product(id):
  pass
