#!/usr/bin/python3
"""
First city model

Uses SQLAlchemy
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class City(Base):
    """
    This will be the state class that links to the table
    'cities'
    """
    __tablename__ = 'cities'

    id = Column(
            Integer, primary_key=True,
            autoincrement=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id'))
