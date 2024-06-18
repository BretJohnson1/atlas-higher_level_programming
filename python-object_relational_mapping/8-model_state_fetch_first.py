#!/usr/bin/python3
"""This module creates a connection to a SQL server"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":

    """Set arguments"""
    username = sys.argv[1]
    password = sys.argv[2]
    dbase = sys.argv[3]

    """Create the engine/establish connection"""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbase}'
        )

    """Set up all data to use"""
    Base.metadata.create_all(engine)

    """Bind the engine to the session"""
    Session = sessionmaker(bind=engine)

    """Create the session"""
    session = Session()

    """Query the data and list the first result, then print"""
    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")

    """Close the session"""
    Session.close()
