#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

def fetch_cities_by_state(username, password, db_name):
    try:
        # Create a database connection
        engine = create_engine(f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}")
        Session = sessionmaker(bind=engine)
        session = Session()

        # Fetch all City objects along with their corresponding State objects
        cities = session.query(City).order_by(City.id).all()

        # Display the results
        for city in cities:
            print(f"{city.id}: {city.name} ({city.state.name})")

        # Close the session
        session.close()

    except Exception as e:
        print(f"Error connecting to the database: {e}")

if __name__ == "__main__":
    # Replace with your actual MySQL credentials and database name
    mysql_username = "your_username"
    mysql_password = "your_password"
    database_name = "hbtn_0e_101_usa"

    fetch_cities_by_state(mysql_username, mysql_password, database_name)