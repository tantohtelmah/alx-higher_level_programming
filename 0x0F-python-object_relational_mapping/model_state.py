#!/usr/bin/env python3
"""
Python file containing the class definition of a State and an instance Base.
"""


from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)
"""
base declaration
"""


if __name__ == "__main__":
    class State(Base):
        """
        Represents a state in the MySQL table 'states'.
        """

        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False,
                    autoincrement=True)
        name = Column(String(128), nullable=False)
