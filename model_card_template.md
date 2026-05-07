# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This is a random forest classifier model using the scikit-learn library created by Eric McCoy. This model is ran with the default scikit-learn hyperparamters with the exception of random_state=42.

## Intended Use
The intended use for this model is to predict whether or not an individual makes more or less than $50,000 per year based on various factors from U.S Census data. The intended users of this model are students in the process of learning Machine Learning.

## Training Data
The model was trained using data from census.csv. This dataset contains more than 32,000 rows of U.S census data. I split the data so 75% of the data was training data while the other 25% was for testing.

## Evaluation Data
The evaluation data is made up of the 25% of data that was not used in the training data.

## Metrics
_Please include the metrics used and your model's performance on those metrics._
The metrics measured in this model are precision, recall, and F1. 
Precision: 0.7378 | Recall: 0.6336 | F1: 0.6817

## Ethical Considerations
The data used in this model contains potentially sensitive information from US Census surveys. The model should not be used in a way that would impact an individuals health or safety.

## Caveats and Recommendations
Data used in this model may be outdated at the time of use and may not accurately represent current income situations.