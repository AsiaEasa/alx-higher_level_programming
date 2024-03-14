#!/usr/bin/python3
"""Takes in the name of a state
as an argument and lists all cities of that state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(
                sys.argv[0]
            )
        )
        exit(1)

    USER = sys.argv[1]
    PASS = sys.argv[2]
    DB = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=USER, passwd=PASS, db=DB)

    cursor = db.cursor()

    Q = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id
            """
    cursor.execute(Q, (sys.argv[4],))

    rows = cursor.fetchall()

    if rows:
        print(", ".join(row[0] for row in rows))
    else:
        print()

    cursor.close()
    db.close()
