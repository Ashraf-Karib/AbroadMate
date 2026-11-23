
import pandas as pd

# Load processed university and programme data
df = pd.read_csv("data/processed/abroadmate_programs.csv")

print("UNIVERSITY FINDER DATA")
print("\nDataset shape:")
print(df.shape)

print("\nAvailable columns:")
print(df.columns.tolist())

print("\nUniversity and programme information:")
print(df[[
    "university_name",
    "country_name",
    "program_name",
    "degree",
    "subject",
    "tuition_fee",
    "currency_code"
]])
