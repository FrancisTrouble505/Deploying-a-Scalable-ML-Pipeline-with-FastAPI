import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np

# TODO: implement the first test. Change the function name and input as needed
def test_score_range():
    """
    # A test that checks that precision, recall, and F1 are between 0 and 1.
    """
    # Your code here
    from ml.model import compute_model_metrics
    y = np.array([0, 0, 0, 1, 1])
    predictions = np.array([0, 0, 1, 1, 1])
    precision, recall, fbeta = compute_model_metrics(y, predictions)
    assert 0 <= precision <= 1
    assert 0 <= recall <= 1
    assert 0 <= fbeta <= 1
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_model_type():
    """
    # Tests that the model used is Random Forest Classifier.
    """
    # Your code here
    from ml.model import train_model
    X = np.array([[1 , 2], [3, 4], [5, 6]])
    y = np.array ([1, 1, 1])
    model = train_model(X, y)
    assert type(model).__name__ == "RandomForestClassifier"
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_data_split():
    """
    # Tests that data split function correctly split the data.
    """
    # Your code here
    from sklearn.model_selection import train_test_split
    data = pd.read_csv("data/census.csv")
    train, test = train_test_split(data, test_size = 0.25, random_state = 42)
    assert len(train) + len(test) == len(data)
    pass
