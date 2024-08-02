# -*- coding: utf-8 -*-
"""KaggleHousePricing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hsydviMgyJg0_KGkoGrtVc0FTwjcZRJM
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

data=pd.read_csv("/content/train.csv")
data

data.columns

data=data.drop(['Street','Alley','Utilities','LandSlope','RoofMatl','PoolQC','GarageYrBlt','GarageFinish'],axis=1)
data

data.isna().sum()

data['LotFrontage']=data['LotFrontage'].fillna(data['LotFrontage'].mean())
data['MasVnrType']=data['MasVnrType'].fillna(data['MasVnrType'].mode()[0])
data['MasVnrArea']=data['MasVnrArea'].fillna(data['MasVnrArea'].mean())
data['BsmtQual']=data['BsmtQual'].fillna(data['BsmtQual'].mode()[0])
data['BsmtCond']=data['BsmtCond'].fillna(data['BsmtCond'].mode()[0])
data['BsmtExposure']=data['BsmtExposure'].fillna(data['BsmtExposure'].mode()[0])
data['BsmtFinType1']=data['BsmtFinType1'].fillna(data['BsmtFinType1'].mode()[0])
data['BsmtFinType2']=data['BsmtFinType2'].fillna(data['BsmtFinType2'].mode()[0])
data['Electrical']=data['Electrical'].fillna(data['Electrical'].mode()[0])
data['FireplaceQu']=data['FireplaceQu'].fillna(data['FireplaceQu'].mode()[0])
data['GarageType']=data['GarageType'].fillna(data['GarageType'].mode()[0])
data['GarageQual']=data['GarageQual'].fillna(data['GarageQual'].mode()[0])
data['GarageCond']=data['GarageCond'].fillna(data['GarageCond'].mode()[0])
data['Fence']=data['Fence'].fillna(data['Fence'].mode()[0])
data['MiscFeature']=data['MiscFeature'].fillna(data['MiscFeature'].mode()[0])

data = pd.get_dummies(data, drop_first=True)

data.head(5)

data.columns

X=data.drop(['SalePrice'],axis=1)
y=data['SalePrice']

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

lasso = Lasso(alpha=0.01)  # Adjust alpha as needed
lasso.fit(x_train, y_train)
selected_features = X.columns[(lasso.coef_ != 0)]

X_train_selected = x_train[selected_features]
X_test_selected = x_test[selected_features]

# Train and Evaluate Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train_selected, y_train)
y_pred_linear = linear_model.predict(X_test_selected)

print("Linear Regression Model:")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_linear)}")
print(f"R^2 Score: {r2_score(y_test, y_pred_linear)}")

# Train and Evaluate Random Forest Regressor
rf_model = RandomForestRegressor()
rf_model.fit(X_train_selected, y_train)
y_pred_rf = rf_model.predict(X_test_selected)

print("\nRandom Forest Regressor Model:")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_rf)}")
print(f"R^2 Score: {r2_score(y_test, y_pred_rf)}")

# Train and Evaluate XGBoost Regressor
xgb_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
xgb_model.fit(X_train_selected, y_train)
y_pred_xgb = xgb_model.predict(X_test_selected)

print("\nXGBoost Regressor Model:")
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred_xgb)}")
print(f"R^2 Score: {r2_score(y_test, y_pred_xgb)}")

testdata=pd.read_csv("/content/test.csv")
testdata

testdata=testdata.drop(['Street','Alley','Utilities','LandSlope','RoofMatl','PoolQC','GarageYrBlt','GarageFinish',],axis=1)
testdata

testdata['LotFrontage']=testdata['LotFrontage'].fillna(testdata['LotFrontage'].mean())
testdata['MasVnrType']=testdata['MasVnrType'].fillna(testdata['MasVnrType'].mode()[0])
testdata['MasVnrArea']=testdata['MasVnrArea'].fillna(testdata['MasVnrArea'].mean())
testdata['BsmtQual']=testdata['BsmtQual'].fillna(testdata['BsmtQual'].mode()[0])
testdata['BsmtCond']=testdata['BsmtCond'].fillna(testdata['BsmtCond'].mode()[0])
testdata['BsmtExposure']=testdata['BsmtExposure'].fillna(testdata['BsmtExposure'].mode()[0])
testdata['BsmtFinType1']=testdata['BsmtFinType1'].fillna(testdata['BsmtFinType1'].mode()[0])
testdata['BsmtFinType2']=testdata['BsmtFinType2'].fillna(testdata['BsmtFinType2'].mode()[0])
testdata['Electrical']=testdata['Electrical'].fillna(testdata['Electrical'].mode()[0])
testdata['FireplaceQu']=testdata['FireplaceQu'].fillna(testdata['FireplaceQu'].mode()[0])
testdata['GarageType']=testdata['GarageType'].fillna(testdata['GarageType'].mode()[0])
testdata['GarageQual']=testdata['GarageQual'].fillna(testdata['GarageQual'].mode()[0])
testdata['GarageCond']=testdata['GarageCond'].fillna(testdata['GarageCond'].mode()[0])
testdata['Fence']=testdata['Fence'].fillna(testdata['Fence'].mode()[0])
testdata['MiscFeature']=testdata['MiscFeature'].fillna(testdata['MiscFeature'].mode()[0])

testdata = pd.get_dummies(testdata, drop_first=True)

testdata.head(5)

testdata.columns

testdata = testdata.reindex(columns=X.columns, fill_value=0)

testdata_selected = testdata[selected_features]

test_predictions=xgb_model.predict(testdata_selected)

test_predictions = np.clip(test_predictions, a_min=0, a_max=None)  # Ensure non-negative predictions
test_predictions = np.nan_to_num(test_predictions, nan=0)  # Replace NaN with 0

submission = pd.DataFrame({
    'Id': testdata['Id'].astype(int),
    'SalePrice': test_predictions.astype(float)})
submission.to_csv('submission.csv', index=False)
print("Predictions for test data have been saved to 'submission.csv'")