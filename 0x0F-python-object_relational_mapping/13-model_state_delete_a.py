#!/usr/bin/python3
"""
Initiation of the code
"""


# 13-model_state_delete_a.py

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)

    # Create a connection to the MySQL server
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name))

    # Create a session to interact with the database
    Base.metadata.create_all(engine)
    session = Session(engine)

    # Query and delete State objects with names containing 'a'
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes and close the session
    session.commit()
    session.close()
