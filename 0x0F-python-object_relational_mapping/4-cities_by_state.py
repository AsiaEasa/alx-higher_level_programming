#!/usr/bin/python3
"""script that lists all cities from
the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    db = MySQLdb.connect(host=localhost,
                         port=3306,
                         user=USER,
                         passwd=PASS,
                         db=DB)

    cursor = db.cursor()
    cursor.execute("SELECT C.id, C.name, S.name",
                      "FROM cities C, states S",
                      "WHERE C.state_id = S.id",
                      "ORDER BY C.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
