#!/usr/bin/python3
"""This module defines a function that creates a connection to a SQL server"""

import MySQLdb
import sys


def safe_state(username, password, dbase, searched):
    """This function imports a database to use"""

    """Establish connection"""
    db = MySQLdb.connect(host="localhost",
                         user=username,
                         passwd=password,
                         database=dbase)

    """Create cursor object and query data"""
    cur = db.cursor()
    sql_cmd = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(sql_cmd, (searched,))

    """Access the queried data to print"""
    rows = cur.fetchall()
    for row in rows:
        print(row)

    """Close the connection and cursor object"""
    cur.close()
    db.close()


if __name__ == "__main__":
    safe_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])