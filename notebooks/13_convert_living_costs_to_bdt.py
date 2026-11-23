
import pandas as pd

# 1. Load datasets
living_costs = pd.read_csv("data/raw/living_costs.csv")
exchange_rates = pd.read_csv("data/raw/exchange_rates.csv")

# 2. Merge living costs with exchange rates
df = pd.merge(
    living_costs,
    exchange_rates,
    on="currency_code",
    how="left"
)

# 3. Convert minimum monthly cost into BDT
df["total_monthly_min_bdt"] = (
    df["total_monthly_min"] * df["bdt_per_unit"]
)

# 4. Convert maximum monthly cost into BDT
df["total_monthly_max_bdt"] = (
    df["total_monthly_max"] * df["bdt_per_unit"]
)

# 5. Save processed dataset
df.to_csv(
    "data/processed/living_costs_bdt.csv",
    index=False
)

# 6. Display results
print("MONTHLY LIVING COSTS IN BDT")

print(
    df[
        [
            "city",
            "currency_code",
            "total_monthly_min_bdt",
            "total_monthly_max_bdt"
        ]
    ].to_string(index=False)
)

print("\nMissing exchange rates:", df["bdt_per_unit"].isnull().sum())

print("\nDataset shape:", df.shape)

print("\nConversion completed!")
