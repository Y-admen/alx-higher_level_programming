#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
Retrieves all states from the database that match
the name passed as argument.
"""

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cursor = db.cursor()
    state_name = argv[4]

    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY %s", (argv[4],)
            )

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
