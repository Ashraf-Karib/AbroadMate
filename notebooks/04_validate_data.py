
import pandas as pd

# Load datasets
countries = pd.read_csv("data/raw/countries.csv")
universities = pd.read_csv("data/raw/universities.csv")
programs = pd.read_csv("data/raw/programs.csv")

print("ABROADMATE DATA VALIDATION")

# 1. Check duplicate programme IDs
print("\n1. Duplicate Programme IDs:")
print(programs["program_id"].duplicated().sum())

# 2. Check missing values
print("\n2. Missing Values:")
print(programs.isnull().sum())

# 3. Check invalid university IDs
invalid_universities = programs[
    ~programs["university_id"].isin(universities["university_id"])
]

print("\n3. Invalid University IDs:")
print(invalid_universities[["program_id", "university_id"]])

# 4. Check invalid tuition fees
programs["tuition_fee"] = pd.to_numeric(
    programs["tuition_fee"], errors="coerce"
)

invalid_fees = programs[
    programs["tuition_fee"].isnull() |
    (programs["tuition_fee"] < 0)
]

print("\n4. Invalid Tuition Fees:")
print(invalid_fees[["program_id", "tuition_fee"]])

# 5. Check invalid country IDs in universities
invalid_countries = universities[
    ~universities["country_id"].isin(countries["country_id"])
]

print("\n5. Invalid Country IDs:")
print(invalid_countries[["university_id", "country_id"]])
