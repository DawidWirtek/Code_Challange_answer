# Module database.py was created to declare basics connected with SQLAlchemy - to cope with FASTApi

# Todo 1.1: Create database using SQLAlchemy

# Importing the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite database URL - db will be created in data directory
SQLALCHEMY_DATABASE_URL = "sqlite:///../data/NY_demographic.db"

# Create engine - for making connection with database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create object that will handle with database using engine - e.g. enable us to add objects to the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create class for creating database models or classes
Base = declarative_base()
