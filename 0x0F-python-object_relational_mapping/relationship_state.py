#!/usr/bin/env python3
"""
Python file containing the class definition of a State and an instance Base.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City

# Creating the declarative base instance
Base = declarative_base()


class State(Base):
    """
    Represents a state in the MySQL table 'states'.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Establish a one-to-many relationship with City objects
    cities = relationship("City", back_populates="state",
                          cascade="all, delete-orphan")
