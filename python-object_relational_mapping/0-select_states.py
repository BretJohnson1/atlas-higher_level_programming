#!/usr/bin/python3
"""This module defines a function that establishes a connection to a SQL server"""

import MySQLdb
import sys


def sql_connect(usr, pw, db_name):
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
        print(row)

    """Close the connection and cursor object"""
    cur.close()
    db.close()


if __name__ == "__main__":
    sql_connect(sys.argv[1], sys.argv[2], sys.argv[3])
