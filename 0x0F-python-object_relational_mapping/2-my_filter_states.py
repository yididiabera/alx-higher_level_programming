#!/usr/bin/python3
"""
A script that provides a searched result from a database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states\
        WHERE BINARY name = '{}'".format(sys.argv[4]))
    rows = c.fetchall()
    [print(row) for row in rows]
