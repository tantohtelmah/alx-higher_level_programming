#!/usr/bin/python3
"""
Initiation of the code
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    username, password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        # Execute SQL query to retrieve states matching the provided name (safe from injection)
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (search_name,))
        states = cursor.fetchall()

        # Display results
        for state in states:
            print(state)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
