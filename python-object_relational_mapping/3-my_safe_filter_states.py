#!/usr/bin/python3
"""
This script will take an argument and display all
values in the states table of hbtn_0e_0_usa
where name matches the argument
"""
import MySQLdb
import sys


def filter_by_input(username, password, database, state):
    """
    filters the input and sets the connection to the
    database
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    select = db.cursor()
    query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
    select.execute(query, (state, ))
    rows = select.fetchall()

    for row in rows:
        print(row)

    select.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    filter_by_input(username, password, database, state)
