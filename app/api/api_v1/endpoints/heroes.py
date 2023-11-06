from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Hero])
def read_heroes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve Heroes.
    """
    heroes = crud.hero.get_multi(db, skip=skip, limit=limit)

    return heroes


@router.post("/", response_model=schemas.Hero)
def create_hero(
    *,
    db: Session = Depends(deps.get_db),
    hero_in: schemas.HeroCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    hero = crud.hero.create_with_owner(db=db, obj_in=hero_in, owner_id=current_user.id)
    return hero


@router.put("/{id}", response_model=schemas.Hero)
def update_hero(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    hero_in: schemas.HeroUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an item.
    """
    hero = crud.hero.get(db=db, id=id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    if not crud.user.is_superuser(current_user) and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    hero = crud.hero.update(db=db, db_obj=hero, obj_in=hero_in)
    return hero


@router.get("/{id}", response_model=schemas.Hero)
def read_hero(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Get item by ID.
    """
    hero = crud.hero.get(db=db, id=id)
    if not hero:
        raise HTTPException(status_code=404, detail="Item not found")
    return hero


@router.delete("/{id}", response_model=schemas.Hero)
def delete_hero(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an item.
    """
    hero = crud.hero.get(db=db, id=id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero = crud.hero.remove(db=db, id=id)
    return hero