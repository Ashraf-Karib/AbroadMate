import pandas as pd

df = pd.read_csv("data/raw/living_costs.csv")

print(df)

print("\nDataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())