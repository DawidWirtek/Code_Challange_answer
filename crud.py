# Module crud.py is stands for: create, read, update and delete
# This module is responsible for all the function that gets data from database

# TODO 1.5: Creating functions for coping with database

from sqlalchemy.orm import Session
from files import models


def get_school_by_categories(db: Session, school_category: str):
    return db.query(models.Data).filter(models.Data.category == school_category).all()
