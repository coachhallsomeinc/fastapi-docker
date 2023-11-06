from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Hero(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    biography = Column(String, index=True)
    about_me = Column(String, index=True)
    image_url = Column(String, index=True)