#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username, password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Create an SQLite engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the provided name (safe from injection)
    state = session.query(State).filter_by(name=search_name).first()

    # Display the result
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Not found")

    # Close the session
    session.close()
