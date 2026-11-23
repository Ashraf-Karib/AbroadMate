
import pandas as pd

# Load the country dataset
countries = pd.read_csv("data/raw/countries.csv")

# Display the dataset
print("COUNTRY DATASET")
print(countries)

# Check dataset dimensions
print("\nDataset Shape:")
print(countries.shape)

# Check column information
print("\nDataset Information:")
print(countries.info())

# Check missing values
print("\nMissing Values:")
print(countries.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(countries.duplicated().sum())
