import pytest
# TODO: add necessary import
import pandas as pd

# TODO: implement the first test. Change the function name and input as needed
def test_data_no_null_value():
    """
    # A test that checks that there are no null values.
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    assert data.isnull().sum().sum() == 0
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_salary_two_values():
    """
    # Tests that the salary column only contains two values.
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    assert len(data["salary"].unique()) == 2
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_data_column_count():
    """
    # Tests that the census data contains 15 columns.
    """
    # Your code here
    data = pd.read_csv("data/census.csv")
    assert data.shape[1] == 15
    pass
