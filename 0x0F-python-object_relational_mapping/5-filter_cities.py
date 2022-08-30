#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                FROM cities\
                JOIN states ON states.id = cities.state_id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC", [sys.argv[4]])
    query_rows = cur.fetchall()
    if query_rows:
        for row in query_rows[0:-1]:
            print("%s, " % row, end='')
        print("%s" % query_rows[-1])
    cur.close()
    conn.close()
