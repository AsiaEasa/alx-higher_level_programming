#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states"""
import sys
import MySQLdb


def ListStates(USER, PASS, DB):
    """Script that takes in arguments and displays all values in the states"""
    db = MySQLdb.connect(host="localhost", port=3306, user=USER, passwd=PASS, db=DB)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: {} <mysql_username> <mysql_password> <database_name>".format(
                sys.argv[0]
            )
        )
        exit(1)

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    ListStates(USER, PASS, DB)
