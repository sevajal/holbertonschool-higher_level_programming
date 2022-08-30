#!/usr/bin/python3
"""script that prints the first State object from
the database hbtn_0e_6_usa"""

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
    state1 = session.query(State).first()
    if state1 is None:
        print("Nothing")
    else:
        print("{}: {}".format(state1.id, state1.name))
    session.close()
