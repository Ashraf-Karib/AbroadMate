
import pandas as pd

# Load datasets
df = pd.read_csv("data/processed/abroadmate_programs.csv")
rates = pd.read_csv("data/raw/exchange_rates.csv")

# Calculate total tuition
df["number_of_semesters"] = df.apply(
    lambda row:
    int(row["program_duration"].split()[0])
    if row["fee_period"] == "Per Semester"
    else None,
    axis=1
)

df["total_program_tuition"] = df.apply(
    lambda row:
    row["tuition_fee"] * row["number_of_semesters"]
    if row["fee_period"] == "Per Semester"
    else row["tuition_fee"],
    axis=1
)

# Merge exchange rates
df = df.merge(
    rates[["currency_code", "bdt_per_unit"]],
    on="currency_code",
    how="left"
)

# Convert tuition into BDT
df["total_tuition_bdt"] = (
    df["total_program_tuition"] * df["bdt_per_unit"]
)

# Display results
print("ABROADMATE - TUITION IN BDT")

print(
    df[
        [
            "program_name",
            "currency_code",
            "total_program_tuition",
            "bdt_per_unit",
            "total_tuition_bdt"
        ]
    ].to_string(index=False)
)
# Save converted dataset
df.to_csv(
    "data/processed/abroadmate_bdt_comparison.csv",
    index=False
)

print("\nBDT comparison saved successfully!")