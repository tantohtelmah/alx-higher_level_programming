#!/usr/bin/python3
"""
Script to list all City objects from the database hbtn_0e_101_usa.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import Base, City
    from relationship_state import State

    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Create connection to MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects sorted by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print results
    for city in cities:
        print("{}: {} ({})".format(city.state.name, city.name, city.id))

    # Close session
    session.close()
