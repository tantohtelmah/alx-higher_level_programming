#!/usr/bin/python3
"""
Script to create State "California" with City "San Francisco" within:
database hbtn_0e_100_usa.
"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_city import City
    from relationship_state import State, Base

    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Create connection to MySQL server
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State "California" and City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close session
    session.close()
