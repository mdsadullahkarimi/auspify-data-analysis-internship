import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the cleaned Netflix dataset
df = pd.read_csv("cleaned_netflix_data.csv")

print("=" * 50)
print("NETFLIX TREND ANALYSIS BY RELEASE YEAR")
print("=" * 50)

# Step 2: Check dataset information
print("\nDataset shape:", df.shape)

print("\nFirst 10 release years:")
print(df["release_year"].head(10))

print("\nMissing release years:", df["release_year"].isna().sum())

# Step 3: Calculate yearly content releases
yearly_counts = (
    df.dropna(subset=["release_year"])
      .groupby("release_year")
      .size()
      .sort_index()
)

print("\nYEAR-WISE NETFLIX CONTENT COUNT")
print(yearly_counts.to_string())

# Step 4: Identify growth and decline trends
yearly_change = yearly_counts.diff()
yearly_growth = yearly_counts.pct_change() * 100

print("\nYEARLY CONTENT CHANGE (LAST 10 YEARS)")
print(yearly_change.tail(10).to_string())

print("\nYEARLY PERCENTAGE CHANGE (LAST 10 YEARS)")
print(yearly_growth.tail(10).round(2).to_string())

# Find the year with the highest content count
peak_year = yearly_counts.idxmax()
peak_count = yearly_counts.max()

print("\nPEAK RELEASE YEAR:", peak_year)
print("HIGHEST CONTENT COUNT:", peak_count)

# Step 5: Create yearly trend visualization
plt.figure(figsize=(12, 6))

plt.plot(
    yearly_counts.index,
    yearly_counts.values,
    marker="o",
    linewidth=2
)

plt.title(
    "Netflix Content Releases by Year",
    fontsize=15,
    fontweight="bold"
)
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()

# Save chart
plt.savefig(
    "Task 4/Task4_Yearly_Trend.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nTrend chart saved: Task4_Yearly_Trend.png")

# Show the chart at the end
# Step 6: Save yearly content ranking

yearly_ranking = yearly_counts.reset_index()

yearly_ranking.columns = ["Release Year", "Content Count"]

yearly_ranking.insert(
    0,
    "Rank",
    range(1, len(yearly_ranking) + 1)
)

yearly_ranking = yearly_ranking.sort_values(
    by="Content Count",
    ascending=False
)

yearly_ranking.to_csv(
    "Task 4/Task4_Yearly_Ranking.csv",
    index=False
)

print("\nYearly ranking saved: Task4_Yearly_Ranking.csv")


plt.show()
