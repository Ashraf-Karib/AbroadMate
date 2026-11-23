
import pandas as pd

# 1. Load processed dataset
df = pd.read_csv("data/processed/abroadmate_programs.csv")

# 2. Extract number of semesters
df["number_of_semesters"] = df.apply(
    lambda row:
    int(row["program_duration"].split()[0])
    if row["fee_period"] == "Per Semester"
    else None,
    axis=1
)

# 3. Calculate total programme tuition
df["total_program_tuition"] = df.apply(
    lambda row:
    row["tuition_fee"] * row["number_of_semesters"]
    if row["fee_period"] == "Per Semester"
    else row["tuition_fee"],
    axis=1
)

# 4. Display results
print("TOTAL PROGRAMME TUITION")

print(
    df[
        [
            "program_name",
            "program_duration",
            "tuition_fee",
            "fee_period",
            "number_of_semesters",
            "total_program_tuition",
            "currency_code"
        ]
    ].to_string(index=False)
)
