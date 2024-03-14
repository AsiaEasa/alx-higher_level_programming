#!/usr/bin/python3
"""takes in the name of a state 
as an argument and lists all cities of that state
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    if len(argv) != 5:
         print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>"
               .format(argv[0]))
         exit(1)

    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    db = MySQLdb.connect(host=localhost,
                         port=3306,
                         user=USER,
                         passwd=PASS,
                         db=DB)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM cities AS c",
                      "INNER JOIN states AS s",
                      "JOIN states ON cities.state_id = states.id",
                      "ON c.state_id = s.id",
                      "ORDER BY c.id")

    rows = cursor.fetchall()
    filtered_cities = [city[2] for city in rows if city[4] == sys.argv[4]]
    print(", ".join(filtered_cities))

    cursor.close()
    db.close()
