#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states
"""
import sys
import MySQLdb

def ListStates (USER, PASS, DB):
    """script that takes in arguments and displays all values in the states
    """
    db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=USER,\
            passwd=PASS,\
            db=DB)
    cursor = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == '__main__':

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    ListStates(USER, PASS, DB)
