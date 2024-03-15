#!/usr/bin/python3
"""Takes in the name of a state
as an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=USER,
        passwd=PASS,
        db=DB
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM cities as ct \
                INNER JOIN states as s \
                   ON ct.state_id = s.id \
                ORDER BY ct.id"
    )
    print(", ".join([ct[2] for ct in c.fetchall() if ct[4] == sys.argv[4]]))
    db.close()
