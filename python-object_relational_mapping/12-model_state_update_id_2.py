#!/usr/bin/python3
"""
Inserts the state 'Louisiana' into db hbtn_0e_6_usa
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

    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    update_state = session.query(State).filter_by(id=2).first()

    if update_state:
        update_state.name = "New Mexico"

        session.commit()

    session.close()
