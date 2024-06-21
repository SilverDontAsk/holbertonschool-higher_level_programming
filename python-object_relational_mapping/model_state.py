#!/usr/bin/python3
"""
First state model

Uses SQLAlchemy
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    This will be the state class that links to the table
    'states'
    """
    __tablename__ = 'states'

    id = Column(
            Integer, primary_key=True,
            autoincrement=True,
            nullable=False)
    name = Column(String(128), nullable=False)
