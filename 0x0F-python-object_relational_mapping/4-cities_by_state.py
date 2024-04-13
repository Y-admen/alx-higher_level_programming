#!/usr/bin/python3
from sys import argv
import MySQLdb
"""
Prints all cities from the database that are in a given state.
"""


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC""")

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
