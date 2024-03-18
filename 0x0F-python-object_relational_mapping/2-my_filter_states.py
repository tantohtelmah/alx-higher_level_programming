#!/usr/bin/python3
"""
Initialisation of code
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and search argument from command line arguments
    username, password, db_name, search_arg = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name, charset="utf8")
    cursor = db.cursor()

    # Create the SQL query using format
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (f"{search_arg}%",))  # Use %s as a placeholder for the search argument

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the database connection
    cursor.close()
    db.close()
