from sqlalchemy.orm import Session
import models, schemas

def create_hero(db: Session, hero: schemas.HeroModel):
    db_hero = models.Hero(name=hero.name, biography=hero.biography, about_me=hero.about_me, image_url=hero.image_url | None )
    db.add(db_hero)
    db.commit()
    db.refresh(db_hero)
    return db_hero

def read_heroes(db: Session):
    return db.query(models.Hero).join(models.Ability, models.Hero.id == models.Ability.hero_id).join(models.AbilityType, models.AbilityType.id == models.Ability.ability_type_id).all()