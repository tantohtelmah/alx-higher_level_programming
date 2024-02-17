#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLite engine
    engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    if state:
        # Change the name to "New Mexico"
        state.name = "New Mexico"
        session.commit()
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
