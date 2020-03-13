import datetime
import string
import random
import pandas as pd
from pprint import pprint

from job_industries import job_industries

# Configurations
total_NRIC_for_group = 1000


# Helper functions goes here
def get_nric_year_representation(year_born: int):
    nric_year = str(year_born)[2:4]
    nric_year_padded = str(nric_year).ljust(7, "0")

    return int(nric_year_padded)


def get_nric_range(from_year_born: int, to_year_born: int):
    return (
        get_nric_year_representation(from_year_born),
        get_nric_year_representation(to_year_born),
    )


def get_fake_NRIC(numbers_of_NRIC: int, from_year_born: int, to_year_born: int):
    range_from, range_to = get_nric_range(from_year_born, to_year_born)

    nric_array = [
        str(random.randint(range_from, range_to)) for _ in range(numbers_of_NRIC)
    ]

    return [
        "".join(["S", nric, random.choice(string.ascii_uppercase)])
        for nric in nric_array
    ]


def get_random_job_gender_income():
    job, income_by_gender = random.choice(list(job_industries.items()))
    gender, income = random.choice(list(income_by_gender.items()))

    return job, gender, income


# The entry point function
def azureml_main():
    # Execution logic goes here
    # Young NRICs
    young_nric_list = get_fake_NRIC(total_NRIC_for_group, 1976, 1999)

    # Middle NRICs
    middle_nric_list = get_fake_NRIC(total_NRIC_for_group, 1964, 1975)

    # Elder NRICs
    elder_nric_list = get_fake_NRIC(total_NRIC_for_group, 1940, 1965)

    # Initialize the DataFrames to return
    df = pd.DataFrame(columns=["NRIC", "page_id", "time_spent"])

    user_features = pd.DataFrame(
        columns=["NRIC", "age", "gender", "job_industry", "income"]
    )

    # Generate each row of data for item in young_nric_list
    for each_nric in young_nric_list:
        for _ in range(random.randint(5, 8)):
            each_nric_row = pd.DataFrame(
                [
                    {
                        "NRIC": each_nric,
                        "page_id": random.randint(0, 8),
                        "time_spent": random.randint(1, 20),
                    }
                ]
            )
            df = df.append(each_nric_row, ignore_index=True)

    # Generate each row of data for item in middle_nric_list
    for each_nric in middle_nric_list:
        for _ in range(random.randint(5, 8)):
            each_nric_row = pd.DataFrame(
                [
                    {
                        "NRIC": each_nric,
                        "page_id": random.randint(0, 8),
                        "time_spent": random.randint(1, 20),
                    }
                ]
            )
            df = df.append(each_nric_row, ignore_index=True)

    # Generate each row of data for item in elder_nric_list
    for each_nric in elder_nric_list:
        for _ in range(random.randint(5, 8)):
            each_nric_row = pd.DataFrame(
                [
                    {
                        "NRIC": each_nric,
                        "page_id": random.randint(0, 8),
                        "time_spent": random.randint(1, 20),
                    }
                ]
            )
            df = df.append(each_nric_row, ignore_index=True)

    # Remove duplicates
    df.sort_values("time_spent", inplace=True)
    df.drop_duplicates(subset=["NRIC", "page_id"], keep="last", inplace=True)

    # Return value must be of a sequence of pandas.DataFrame
    return df


if __name__ == "__main__":
    df = azureml_main()

    # data.csv contains NRIC, page_id, time_spent
    # df.to_csv("data.csv", index=False)

