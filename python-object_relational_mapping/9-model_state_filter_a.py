#!/usr/bin/python3
"""
filters the State objects from database hbtn_0e_6_usa
that contain the letter 'a'

uses SQLAlchemy
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    filter_L = 'a'

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(
            State.name.like(
                f'%{filter_L}%')
            ).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
