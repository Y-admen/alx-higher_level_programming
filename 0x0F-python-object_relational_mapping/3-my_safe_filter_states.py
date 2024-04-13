#!/usr/bin/python3
import MySQLdb
from sys import argv

"""
Connects to the MySQL database, filters the states table by name,
and prints the results.
"""


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cursor = db.cursor()
    state_name = argv[4]

    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC;", (state_name,)
    )

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
