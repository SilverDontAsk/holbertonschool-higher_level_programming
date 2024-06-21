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
    qy = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state)
    select.execute(qy)
    rows = select.fetchall()

    for row in rows:
        print(row)

    select.close()
    db.close()


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    filter_by_input(username, password, database, state)
