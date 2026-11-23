
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed dataset
df = pd.read_csv("data/processed/abroadmate_programs.csv")

sns.set_theme(style="whitegrid")


# Chart 1: Programmes by country
plt.figure(figsize=(8, 5))

ax = sns.countplot(
    data=df,
    x="country_name"
)

# Display count above each bar
for container in ax.containers:
    ax.bar_label(container)

plt.title("Number of Master's Programmes by Country")
plt.xlabel("Country")
plt.ylabel("Number of Programmes")
plt.tight_layout()
plt.savefig("data/processed/programmes_by_country.png")
plt.show()





# Chart 2: Published tuition amounts
plt.figure(figsize=(12, 6))

ax = sns.barplot(
    data=df,
    x="tuition_fee",
    y="program_name"
)

# Add labels after each bar
for i, row in df.reset_index(drop=True).iterrows():
    ax.text(
        row["tuition_fee"] + 500,
        i,
        f'{row["currency_code"]} | {row["fee_period"]}',
        va="center",
        fontsize=10
    )

plt.xlim(0, df["tuition_fee"].max() * 1.35)

plt.title(
    "Published Tuition Amounts by Programme\n"
    "(Different currencies and fee periods)"
)
plt.xlabel("Tuition Amount (local currency)")
plt.ylabel("Programme")
plt.tight_layout()

plt.savefig("data/processed/tuition_by_programme.png")
plt.show()


print("Both charts saved successfully!")
