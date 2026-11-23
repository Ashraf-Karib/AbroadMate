
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load processed dataset
df = pd.read_csv("data/processed/living_costs_bdt.csv")

# 2. Select records with available minimum totals
chart_data = df.dropna(subset=["total_monthly_min_bdt"]).copy()

# 3. Sort cities by minimum monthly cost
chart_data = chart_data.sort_values(
    by="total_monthly_min_bdt"
)

# 4. Create visualization
plt.figure(figsize=(12, 7))

sns.barplot(
    data=chart_data,
    x="total_monthly_min_bdt",
    y="city"
)
for index, value in enumerate(chart_data["total_monthly_min_bdt"]):
    plt.text(
        value + 2000,
        index,
        f"BDT {value:,.0f}",
        va="center"
    )
plt.title("Estimated Minimum Monthly Living Cost by City")
plt.xlabel("Monthly Cost (BDT)")
plt.ylabel("City")

plt.ticklabel_format(
    style="plain",
    axis="x"
)

plt.tight_layout()
plt.savefig(
    "assets/living_cost_minimum_bdt.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
