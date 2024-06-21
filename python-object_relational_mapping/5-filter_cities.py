#!/usr/bin/python3
"""
takes the name of a state as an argument and lists
the cities of that state using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


def list_cities_by_input(username, password, database, state):
    """
    sets up a connection to hbtn_0e_4_usa and grab an input
    to list cities off of
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
    select = db.cursor()
    qr = """
    SELECT GROUP_CONCAT(name SEPARATOR ', ')
    FROM cities
    WHERE state_id IN (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC
    """
    select.execute(qr, (state, ))

    cities_string = select.fetchone()
    if cities_string[0]:
        print(cities_string[0])
    else:
        print()

    select.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    list_cities_by_input(username, password, database, state)
