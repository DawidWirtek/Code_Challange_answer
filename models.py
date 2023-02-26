# Module models.py was created for declaring classes (models) that will be interacting with database

# Todo 1.2: Create database scheme using SQLAlchemy - scheme based on dataset

# Importing the SQLAlchemy parts
from sqlalchemy import Column, Integer, String, Text
from database import Base

# Create constant variable from dataset
YEAR = "2015-16"


# Create database scheme - each of attributes represents a column in database table
# In table there is one primary key, which is set automatically thanks to sqlalchemy module
class Data(Base):
    __tablename__ = "demographic_data"

    index_label = Column(Integer, primary_key=True)

    dbn = Column(Text, nullable=False)
    school_name = Column(String, nullable=False)

    category = Column(String, nullable=False)

    total_enrollment = Column(Integer, nullable=False)

    female = Column(Text, nullable=False)
    male = Column(Text, nullable=False)

    asian = Column(Text, nullable=False)
    black = Column(Text, nullable=False)
    hispanic = Column(Text, nullable=False)
    other = Column(Text, nullable=False)
    white = Column(Text, nullable=False)

    ela_test_takers = Column(Text, nullable=False)
    ela_level_1 = Column(Text, nullable=False)
    ela_level_2 = Column(Text, nullable=False)
    ela_level_3 = Column(Text, nullable=False)
    ela_level_4 = Column(Text, nullable=False)

    math_test_takers = Column(Text, nullable=False)
    math_level_1 = Column(Text, nullable=False)
    math_level_2 = Column(Text, nullable=False)
    math_level_3 = Column(Text, nullable=False)
    math_level_4 = Column(Text, nullable=False)
