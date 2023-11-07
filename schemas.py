from typing import Optional

from pydantic import BaseModel, EmailStr

class AbilityTypeModel(BaseModel):
    id: int
    name: str

class AbilityModel(BaseModel):
    id: int
    hero_id: int
    ability_type_id: int 

class RelationshipTypeModel(BaseModel):
    id: int
    name: str

class RelationshipModel(BaseModel):
    id: int
    hero1_id: int
    hero2_id: int   

class HeroModel(BaseModel):
    id: int
    name: str | None
    about_me: str | None
    biography: str | None
    image_url: str | None
    abilities: list[AbilityModel] = []
    followers: list[RelationshipModel] = []
    follows: list[RelationshipModel]= []

    class Config:
        orm_mode = True

class ResponseModel(BaseModel):
    hero: HeroModel
    ability: AbilityModel
    ability_type: AbilityTypeModel