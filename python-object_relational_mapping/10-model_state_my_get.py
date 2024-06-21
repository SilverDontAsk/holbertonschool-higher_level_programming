#!/usr/bin/python3
"""
prints the state object with the name passed as an argument
from db hbtn_0e_6_usa
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
    state_arg = sys.argv[4]

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(
            State.name == state_arg).first()

    if state is None:
        print("Not found")
    else:
        print(f"{state.id}")

    session.close()
