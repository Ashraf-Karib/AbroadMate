
import pandas as pd

# Load processed dataset
df = pd.read_csv("data/processed/abroadmate_programs.csv")

print("ABROADMATE - EXPLORATORY DATA ANALYSIS")

# 1. Dataset overview
print("\n1. Dataset Overview")
print("Total programmes:", len(df))
print("Total universities:", df["university_name"].nunique())
print("Total countries:", df["country_name"].nunique())

# 2. Programmes by country
print("\n2. Programmes by Country")
print(df["country_name"].value_counts())

# 3. Programmes by university
print("\n3. Programmes by University")
print(df["university_name"].value_counts())

# 4. Tuition fees grouped by currency and fee period
print("\n4. Tuition Fee Overview")
fee_summary = df.groupby(
    ["currency_code", "fee_period"]
)["tuition_fee"].agg(["count", "min", "max", "mean"])

print(fee_summary)

# 5. Display programme names
print("\n5. Available Programmes")
print(df[["program_name", "university_name", "country_name"]])
