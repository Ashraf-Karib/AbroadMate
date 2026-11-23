import pandas as pd

# Load datasets
countries = pd.read_csv("data/raw/countries.csv")
universities = pd.read_csv("data/raw/universities.csv")

print("COUNTRIES DATASET")
print(countries.head())

print("\nUNIVERSITIES DATASET")
print(universities.head())

print("\nUniversity Dataset Shape:")
print(universities.shape)

print("\nUniversities per Country:")
print(universities["country_id"].value_counts())

# Check whether country IDs exist
invalid_ids = universities[
    ~universities["country_id"].isin(countries["country_id"])
]

print("\nInvalid Country IDs:")
print(invalid_ids)