#!/usr/bin/python3
"""This module defines a function that creates a connection to a SQL server"""

import MySQLdb
import sys


def cities(username, password, dbase):
    """This function imports a database to use"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         database=dbase)

    """Create cursor object and query data"""
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON cities.state_id = states.id")

    """Access the queried data to print"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """Close the connection and cursor object"""
    cur.close()
    db.close()


if __name__ == "__main__":
    cities(sys.argv[1], sys.argv[2], sys.argv[3])