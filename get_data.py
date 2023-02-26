# Module get_data.py is responsible for:
# - downloading data from browser url
# - reformat data to desire format
# - load data into database

# TODO 1.3: Creating module for loading dataset into database

from files import database
import pandas as pd
import requests


# URL source for downloading csv file of dataset
CSV_URL = "https://data.cityofnewyork.us/api/views/7yc5-fec2/rows.csv?accessType=DOWNLOAD"


def get_data_to_db():
    # Using requests library for downloading file
    with requests.Session() as s:

        # Getting content from particular URL
        download = s.get(CSV_URL)
        # Decoding content using utf-8 unicode
        decoded_content = download.content.decode('utf-8')

    # Creating file in particular directory as csv file
    with open("../data/original_data.csv", mode="w") as file:
        file.write(decoded_content)

    # Using pandas for dealing with data - creating dataframe
    original_data = pd.read_csv("../data/original_data.csv")

    # Getting rid of columns which consists words such as: %, Grade, +, ELL, Year
    # The reason for that is to get only desire information
    column_to_delete = [column for column in original_data
                        if (("%" in column) or ("Grade" in column) or ("+" in column))
                        or ("ELL" in column) or ("Year" in column)]
    data_after_deleting_column = original_data.drop(columns=column_to_delete)

    # Setting appropriate format for column names
    # The purpose: pass dataframe to sql later - names in dataframe corresponds to names in database scheme
    formatted_name_of_columns = [column.replace("#", "") for column in data_after_deleting_column.keys()]
    formatted_name_of_columns = [column.replace(" ", "_").lower() for column in formatted_name_of_columns]

    # Setting formatted name of column to dataframe with desire information
    data_after_deleting_column.columns = formatted_name_of_columns

    # Changing some information in dataset
    # - whenever letter s appeared in dataframe No Data is set
    for column in data_after_deleting_column:
        data_after_deleting_column[column] = data_after_deleting_column[column].replace("s", "No Data")

    # - if cells don't have value setting No Data
    data_after_deleting_column.fillna("No Data", inplace=True)

    # Saving formatted data into csv in desire directory - without indexes
    data_after_deleting_column.to_csv("../data/data_after_cleaning.csv", index=False)

    # Change of variable name to easier usage
    data = data_after_deleting_column

    # Saving formatted data into database in desire directory
    # Using engine, if table with "demographic_data" exists data is replaced, without indexes
    data.to_sql("demographic_data", con=database.engine, if_exists="replace", index_label="id")
