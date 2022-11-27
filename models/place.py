#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv

from sqlalchemy.orm import relationship
import models
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Integer, Float
from sqlalchemy import Column
from sqlalchemy import ForeignKey

from models.review import Review


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms =  Column(Integer, default=0, nullable=False)
    max_guest =  Column(Integer, default=0, nullable=False)
    price_by_night =  Column(Integer, default=0, nullable=False)
    latitude =  Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")



    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def review(self):
            """ getter attribute reviews that returns
                the list of Review instances with place_id equals 
                to the current Place.id
                => It will be the FileStorage relationship between 
                Place and Review
            """
            list_review = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    list_review.append(review)
            return(list_review)
