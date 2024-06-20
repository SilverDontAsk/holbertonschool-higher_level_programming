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


def filter_all_states(username, password, database):
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
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    filter_all_states(username, password, database)
