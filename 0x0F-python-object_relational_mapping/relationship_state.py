#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    class State in relation with city
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    # Other state-related columns go here

    # Establish a one-to-many relationship with cities
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
