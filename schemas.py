# Module schemas.py is responsible for:
# - declaring type of particular variable

# TODO 1.4: Creating type check class using pydantic

from pydantic import BaseModel


class SchoolData(BaseModel):
    id: int

    dbn: str
    school_name: str

    category: str

    total_enrollment: str

    female: str
    male: str

    asian: str
    black: str
    hispanic: str
    other: str
    white: str

    ela_test_takers: str
    ela_level_1: str
    ela_level_2: str
    ela_level_3: str
    ela_level_4: str

    math_test_takers: str
    math_level_1: str
    math_level_2: str
    math_level_3: str
    math_level_4: str

    class Config:
        orm_mode = True
