#!/usr/bin/python3
"""
Script that lists all State objects and corresponding City objects
contained in the database hbtn_0e_101_usa.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import Base, City
    from relationship_state import State

    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Create connection to MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects sorted by states.id
    states = session.query(State).order_by(State.id).all()

    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    # Close session
    session.close()
