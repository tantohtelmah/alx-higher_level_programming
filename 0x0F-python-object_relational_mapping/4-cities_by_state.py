#!/usr/bin/python3
"""
Initiation of the code
"""


import MySQLdb
import sys

if __name__ == "__main__":
    
    # Get MySQL credentials from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        # Execute SQL query to retrieve all cities
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        cities = cursor.fetchall()

        # Display results
        for city in cities:
            print(city)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
