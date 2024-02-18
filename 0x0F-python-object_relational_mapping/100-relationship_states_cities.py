#!/usr/bin/python3
"""
Initiation of the code
"""


# 100-relationship_states_cities.py

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(argv) != 3:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)

    # Create a connection to the MySQL server
    username, password, db_name = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name))

    # Create tables if they don't exist
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State "California" and City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the State and City to the session
    session.add(california)
    session.add(san_francisco)

    # Commit the changes and close the session
    session.commit()
    session.close()
