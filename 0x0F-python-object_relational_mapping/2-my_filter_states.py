#!/usr/bin/python3
"""
Retrieves all states from the database that match
the name passed as argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cursor = db.cursor()
    state_name = argv[4]

    cursor.execute(
            """SELECT * FROM states WHERE name LIKE BINARY '{}'
            ORDER BY id ASC""".format(argv[4])
            )

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
