
import pandas as pd

# Load all datasets
countries = pd.read_csv("data/raw/countries.csv")
universities = pd.read_csv("data/raw/universities.csv")
programs = pd.read_csv("data/raw/programs.csv")

# Merge programs with universities
program_details = programs.merge(
    universities[["university_id", "university_name", "country_id"]],
    on="university_id",
    how="left"
)

# Merge with countries
program_details = program_details.merge(
    countries[["country_id", "country_name"]],
    on="country_id",
    how="left"
)

# Display important information
print("ABROADMATE PROGRAMME DATABASE")

print(
    program_details[
        [
            "program_id",
            "program_name",
            "university_name",
            "country_name",
            "tuition_fee",
            "currency_code"
        ]
    ].to_string(index=False)
)

# Check missing university or country matches
print("\nMissing University Names:")
print(program_details["university_name"].isnull().sum())

print("\nMissing Country Names:")
print(program_details["country_name"].isnull().sum())
