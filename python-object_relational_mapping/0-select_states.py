#!/usr/bin/python3
"""
This is a script that lists all the states that are
in the database hbtn_0e_usa

It takes 3 arguments, username, password and database

All result is in ascending order
"""
import MySQLdb
import sys


def list_all_states(username, password, name):
    """
    This will connect to the MySql server and list all
    states in ascending order sorted by states.id
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    select = db.cursor()
    select.execute("Select id, name FROM states ORDER BY id ASC")
    rows = select.fetchall()

    for row in rows:
        print(row)

    select.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_all_states(username, password, database)
