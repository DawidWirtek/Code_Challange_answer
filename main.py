# This main.py module is the main file that connects all modules from 1.1 to 1.5

# TODO 1.6: Creating file that creates working server with some functionality defines in crud module

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from files import crud, models, schemas
from database import SessionLocal, engine
from get_data import get_data_to_db

# For creating all metadata
models.Base.metadata.create_all(bind=engine)

# Creating app that will handle all API requests
app = FastAPI()


# Function for creating independent connection with each requests
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Download data from URL and create database function
get_data_to_db()


# List of available category:
list_of_categories = ["All Students",
                      "Attend school outside district of residence",
                      "English Language Learners",
                      "Poverty",
                      "Reside in temporary housing",
                      "Students with Disabilities"]


# Directory for dealing with filtered category - not working:(
@app.get("/school/{category}", response_model=schemas.SchoolData)
def get_school(category: str, db: Session = Depends(get_db)):
    if category not in list_of_categories:
        raise HTTPException(status_code=404, detail="Pass correct category")
    else:
        db_schools_by_category = crud.get_school_by_categories(db=db, school_category=category)
    return db_schools_by_category
