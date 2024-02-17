#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLite engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State objects containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display results
    if states:
        for state in states:
            print(f"{state.id}: {state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
