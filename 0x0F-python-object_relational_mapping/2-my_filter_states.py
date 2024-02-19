#!/usr/bin/python3
"""
Initiation of the code
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        exit(1)

    # Get MySQL credentials and state name from command line arguments
    username, password, db_name, search_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=db_name)
        cursor = db.cursor()

        # Execute query to retrieve states matching the provided name
        q = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(q, (f"{search_name}%",))
        states = cursor.fetchall()

        # Display results
        for row in states:
            state_id, state_name = row
            print(f"{state_id}: {state_name}")

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")
