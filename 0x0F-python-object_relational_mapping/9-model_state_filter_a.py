#!/usr/bin/python3
"""script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
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
    for state in session.query(State).order_by(State.id).all():
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()
