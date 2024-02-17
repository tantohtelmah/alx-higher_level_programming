#!/usr/bin/python3
"""
Initiation of the code
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username, password = sys.argv[1], sys.argv[2]
    db_name, search_name = sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        # Execute SQL query (safe from injection)
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                 ORDER BY cities.id ASC"
        cursor.execute(query, (search_name,))
        cities = cursor.fetchall()

        # Display results
        for city in cities:
            print(city)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
