#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
     # Check if all required arguments are provided
    if len(sys.argv) != 3:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        exit(1)
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLite engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for Louisiana
    louisiana = State(name="Louisiana")

    # Add the State object to the session
    session.add(louisiana)
    session.commit()

    # Print the new states.id
    print(louisiana.id)

    # Close the session
    session.close()
