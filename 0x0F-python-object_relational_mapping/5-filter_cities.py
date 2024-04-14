#!/usr/bin/python3
"""
Module that lists all cities of a given state from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2],
        db=argv[3]
    )
    state_name = argv[4]
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name=%s ORDER BY id ASC""", (state_name,)
                   )

    cities = cursor.fetchall()

    print(",".join([row[1] for row in cities]))

    db.close()
