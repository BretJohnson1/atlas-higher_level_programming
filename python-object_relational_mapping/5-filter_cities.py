#!/usr/bin/python3
"""This module defines a function that creates a connection to a SQL server"""

import MySQLdb
import sys


def cities_for_state(username, password, dbase):
    """This function imports a database to use"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         database=dbase)

    """Create cursor object and query data"""
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
        = states.id WHERE states.name LIKE %s ORDER BY cities.id\
        ", (sys.argv[4],))

    """Access the queried data to print"""
    print(", ".join(rows[0] for rows in cur.fetchall()))

    """Close the connection and cursor object"""
    cur.close()
    db.close()


if __name__ == "__main__":
    cities_for_state(sys.argv[1], sys.argv[2], sys.argv[3])
