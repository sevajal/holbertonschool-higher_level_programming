#!/usr/bin/python3
"""Script that prints all City objects from the database hbtn_0e_14_usa"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    a1 = sys.argv[1]
    a2 = sys.argv[2]
    a3 = sys.argv[3]
    en = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(a1, a2, a3),
                       pool_pre_ping=True)
    Base.metadata.create_all(en)
    session = Session(en)
    for row in session.query(State.name, City.id, City.name).join(
                             City).order_by(City.id).all():
        print("{}: ({}) {}".format(row[0], row[1], row[2]))
    session.close()
