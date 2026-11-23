
import pandas as pd

# Load datasets
countries = pd.read_csv("data/raw/countries.csv")
universities = pd.read_csv("data/raw/universities.csv")
programs = pd.read_csv("data/raw/programs.csv")

# Merge programmes and universities
df = programs.merge(
    universities[
        ["university_id", "university_name", "country_id"]
    ],
    on="university_id",
    how="left"
)

# Merge countries
df = df.merge(
    countries[["country_id", "country_name"]],
    on="country_id",
    how="left"
)

# Save processed dataset
df.to_csv(
    "data/processed/abroadmate_programs.csv",
    index=False
)

print("Processed dataset saved successfully!")
print("Dataset shape:", df.shape)
print("\nFinal columns:")
print(df.columns.tolist())
