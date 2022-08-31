#!/usr/bin/python3
"""script that lists all City objects from the database hbtn_0e_101_usa"""

import sys
from relationship_state import Base, State
from relationship_city import City
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
    for State in session.query(City.id, City.name, State.name).join(
                               State).order_by(City.id).all():
        print("{}: {} -> {}".format(State[0], State[1], State[2]))
    session.close()
