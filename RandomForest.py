# Code you have previously used to load data
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# Path of the file to read
file_path = 'melb_data.csv'

home_data = pd.read_csv(file_path)

home_data['BuildingArea'] = home_data['BuildingArea'].fillna(0)
home_data['YearBuilt'] = home_data['YearBuilt'].fillna(2000)


# Create target object and call it y
y = home_data.Price
# Create X
features = ['BuildingArea', 'YearBuilt', 'Rooms', 'Bedroom2', 'Bathroom', 'Landsize', 'Propertycount']
X = home_data[features]



# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
housingDataModel = DecisionTreeRegressor(random_state=1)
# Fit Model
housingDataModel.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = housingDataModel.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

# Using best value for max_leaf_nodes
housingDataModel = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
housingDataModel.fit(train_X, train_y)
val_predictions = housingDataModel.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))


# Set up code checking
print("\nSetup complete")

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error

# Define the model. Set random_state to 1
rf_model = RandomForestRegressor(random_state=1)

# fit your model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of your Random Forest model on the validation data
rf_val_predict = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predict, val_y)
rf_val_percent_mae = 100 - mean_absolute_percentage_error(rf_val_predict, val_y)
#print(len(rf_val_predict))
#print(rf_val_predict)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))
print("The percentage of Validation for Random Forest Model: {}".format(rf_val_percent_mae))
#print(rf_val_predict/rf_val_mae*100)
