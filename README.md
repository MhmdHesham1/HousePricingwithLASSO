House Price Prediction
Description

This project predicts house prices using Lasso Regression for feature selection and XGBoost for modeling.
Files

    train.csv: Training data with features and target (SalePrice).
    test.csv: Test data with features (no target).
    submission.csv: Output file with predictions for the test data.
    README.md: Project documentation.

Requirements

    Python 3.x
    pandas
    numpy
    scikit-learn
    xgboost

Installation

To install the required libraries, run:
  pip install pandas numpy scikit-learn xgboost

Steps

    Load Data: Read the training and test data.
    Preprocessing:
        Combine train and test data for preprocessing.
        Drop unnecessary columns.
        Fill missing values.
        One-hot encode categorical features.
    Feature Selection: Use Lasso Regression to select important features.
    Model Training: Train an XGBoost model using the selected features.
    Prediction: Predict house prices for the test data.
    Submission: Save the predictions to submission.csv.

Running the Code

To run the code, execute the script in a Python environment after ensuring all dependencies are installed. The predictions will be saved in the submission.csv file.
