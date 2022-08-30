#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
where name matches the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities\
                JOIN states ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
