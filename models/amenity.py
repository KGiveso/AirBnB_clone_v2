#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Created Amenity class"""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = \
        relationship('Place', secondary='place_amenity', viewonly=False)
