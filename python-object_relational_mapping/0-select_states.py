#!/usr/bin/python3

import MySQLdb
import sys


def list_all_states(username, password, database):
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(f"({row[0]}, '{row[1]}')")
    cursor.close()
    db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
