#!/usr/bin/python3
"""
Connects to a MySQL database and lists all states from the database.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    cursor = db.cursor()

    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                   ORDER BY id ASC;""")

    states = cursor.fetchall()

    for state in states:
        print(state)

    db.close()
