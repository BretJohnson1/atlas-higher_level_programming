#!/usr/bin/python3
"""This module defines a function that creates a connection to a SQL server"""

import MySQLdb
import sys


def print_n_state(usr, pw, db_name):
    """This function imports a database to use"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost",
                         user=usr,
                         port=3306,
                         passwd=pw,
                         database=db_name)

    """Create cursor object"""
    cur = db.cursor()
    cur.execute("SELECT * FROM states;")

    """Access the queried data to print"""
    rows = cur.fetchall()
    for row in rows:
        if str(row[1]).startswith("N"):
            print(row)

    """Close the connection and cursor object"""
    cur.close()
    db.close()


if __name__ == "__main__":
    print_n_state(sys.argv[1], sys.argv[2], sys.argv[3])
