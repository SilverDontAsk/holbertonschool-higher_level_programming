#!/usr/bin/python3
"""
This script will list all states with a name starting with N
from the database Hbtn_0e_usa

It will take 3 arguments:
    Username
    Password
    Name(Database name)

It will be sorted by states.id in ascending order
"""
import MySQLdb
import sys


def Filter_all_states(username, password, database):
    """
    This function will set up a connection with the database
    and fulfill the function of filtering for the desired
    result
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    select = db.cursor()
    select.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    rows = select.fetchall()
    for row in rows:
        print(row)
    select.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    Filter_all_states(username, password, database)
