
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("data/processed/living_costs_bdt.csv")

# 2. Keep complete records
chart_data = df.dropna(
    subset=[
        "total_monthly_min_bdt",
        "total_monthly_max_bdt"
    ]
).copy()

# 3. Sort by minimum cost
chart_data = chart_data.sort_values(
    by="total_monthly_min_bdt"
).reset_index(drop=True)

# 4. Create chart
plt.figure(figsize=(12, 7))

for index, row in chart_data.iterrows():

    minimum = row["total_monthly_min_bdt"]
    maximum = row["total_monthly_max_bdt"]

    # Draw line from minimum to maximum
    plt.hlines(
        y=index,
        xmin=minimum,
        xmax=maximum,
        linewidth=5
    )

    # Mark minimum and maximum
    plt.scatter(minimum, index, color="blue", s=60)
    plt.scatter(maximum, index, color="orange", s=60)

# 5. Format chart
plt.yticks(
    range(len(chart_data)),
    chart_data["city"]
)

plt.title("Minimum vs Maximum Monthly Living Costs")
plt.xlabel("Monthly Cost (BDT)")
plt.ylabel("City")

plt.scatter([], [], color="blue", label="Minimum")
plt.scatter([], [], color="orange", label="Maximum")
plt.legend()

plt.ticklabel_format(style="plain", axis="x")
plt.tight_layout()
plt.savefig(
    "assets/living_cost_range_bdt.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()