#!/usr/bin/python3
"""
Initiation of the code
"""


from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """
    The Class City. It unherits from the instance base
    and has a Many-to-one relationship with states
    """

    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
    state = relationship('State', back_populates='cities')
