#!/usr/bin/python3
"""This is the City module.

Contains the City class that inherits from Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from relationship_state import Base


class City(Base):
    """This class corresponds to the cities table in our database.

        Attributes:

            id (int): Identifier for the city.
            name (str): Name of the city.
            state_id (int): Identifier for the associated state.
    """

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)