
import pandas as pd

# 1. Load living cost dataset
df = pd.read_csv("data/raw/living_costs.csv")

# 2. Define expense categories
min_columns = [
    "accommodation_min",
    "food_min",
    "transport_min",
    "other_min"
]

max_columns = [
    "accommodation_max",
    "food_max",
    "transport_max",
    "other_max"
]

# 3. Calculate minimum totals only when all categories are available
complete_min = df[min_columns].notna().all(axis=1)

df.loc[complete_min, "total_monthly_min"] = (
    df.loc[complete_min, min_columns].sum(axis=1)
)

# 4. Calculate maximum totals only when all categories are available
complete_max = df[max_columns].notna().all(axis=1)

df.loc[complete_max, "total_monthly_max"] = (
    df.loc[complete_max, max_columns].sum(axis=1)
)

# 5. Save updated dataset
df.to_csv("data/raw/living_costs.csv", index=False)

# 6. Display results
print("MONTHLY LIVING COST TOTALS")

print(
    df[
        [
            "cost_id",
            "city",
            "currency_code",
            "total_monthly_min",
            "total_monthly_max"
        ]
    ].to_string(index=False)
)

print("\nDataset shape:", df.shape)
print("\nCalculation completed!")
