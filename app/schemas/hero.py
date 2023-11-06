from typing import Optional

from pydantic import BaseModel


# Shared properties
class HeroBase(BaseModel):
    name: Optional[str] = None
    biography: Optional[str] = None
    about_me: Optional[str] = None
    image_url: Optional[str] = None


# Properties to receive on item creation
class HeroCreate(HeroBase):
    name: str


# Properties to receive on item update
class HeroUpdate(HeroBase):
    pass


# Properties shared by models stored in DB
class HeroInDBBase(HeroBase):
    id: int
    name: str

    class Config:
        orm_mode = True


# Properties to return to client
class Hero(HeroInDBBase):
    pass


# Properties properties stored in DB
class HeroInDB(HeroInDBBase):
    pass