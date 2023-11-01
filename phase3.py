# Import libraries
import pandas as pd

# Load the dataset
data = pd.read_csv('Electricity.csv')
# Display the first few rows of the dataset
print(data.head())

# Check the data types of each column
print(data.dtypes)

# Summary statistics
print(data.describe())
# Check for missing values
missing_values = data.isnull().sum()
print(missing_values)

# Remove rows with missing values or replace them as needed
data = data.dropna()

# Check for duplicated rows
duplicates = data.duplicated().sum()
print("Number of duplicated rows:", duplicates)

# Remove duplicates if necessary
data = data.drop_duplicates()
# Data transformation steps can include one-hot encoding for categorical variables
#data = pd.get_dummies(data, columns=['categorical_column'])

data.to_csv('preprocessed_electricity_data.csv', index=False)
