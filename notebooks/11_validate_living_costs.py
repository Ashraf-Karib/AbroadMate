
import pandas as pd

# 1. Load datasets
df = pd.read_csv("data/raw/living_costs.csv")
countries = pd.read_csv("data/raw/countries.csv")

print("LIVING COST DATA VALIDATION")

# 2. Check duplicate IDs
print("\nDuplicate Cost IDs:")
print(df["cost_id"].duplicated().sum())

# 3. Check invalid country IDs
invalid_countries = df[
    ~df["country_id"].isin(countries["country_id"])
]

print("\nInvalid Country IDs:")
print(invalid_countries)

# 4. Check negative values
cost_columns = [
    "accommodation_min", "accommodation_max",
    "food_min", "food_max",
    "transport_min", "transport_max",
    "other_min", "other_max",
    "total_monthly_min", "total_monthly_max"
]

negative_values = (df[cost_columns] < 0).sum()

print("\nNegative Values:")
print(negative_values.sum())

# 5. Check minimum and maximum values
pairs = [
    ("accommodation_min", "accommodation_max"),
    ("food_min", "food_max"),
    ("transport_min", "transport_max"),
    ("other_min", "other_max"),
    ("total_monthly_min", "total_monthly_max")
]

print("\nInvalid Minimum-Maximum Pairs:")

for minimum, maximum in pairs:
    invalid = df[
        (df[minimum] > df[maximum])
    ]
    print(f"{minimum} vs {maximum}: {len(invalid)}")

# 6. Check missing essential information
required_columns = [
    "cost_id", "country_id", "city",
    "currency_code", "source_url",
    "verification_status"
]

print("\nMissing Essential Values:")
print(df[required_columns].isnull().sum())

print("\nVALIDATION COMPLETED")
