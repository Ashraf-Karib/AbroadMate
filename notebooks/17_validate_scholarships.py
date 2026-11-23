
import pandas as pd

# Load scholarship dataset
df = pd.read_csv("data/raw/scholarships.csv")

print("SCHOLARSHIP DATA VALIDATION")

# Check dataset shape
print("\nDataset Shape:")
print(df.shape)

# Check duplicate scholarship IDs
print("\nDuplicate Scholarship IDs:")
print(df["scholarship_id"].duplicated().sum())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check invalid country IDs
countries = pd.read_csv("data/raw/countries.csv")

invalid_countries = df[
    df["country_id"].notna() &
    ~df["country_id"].isin(countries["country_id"])
]

print("\nInvalid Country IDs:")
print(invalid_countries[["scholarship_id", "country_id"]])

# Display scholarship names
print("\nAvailable Scholarships:")
print(df["scholarship_name"])
