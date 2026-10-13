
import pandas as pd

# Step 1: Load the cleaned Netflix dataset
df = pd.read_csv("cleaned_netflix_data.csv")

print("=" * 50)
print("NETFLIX COUNTRY-WISE CONTENT ANALYSIS")
print("=" * 50)

print("\nDataset shape:", df.shape)

# Step 2: Extract and clean country information
country_data = df.dropna(subset=["country"]).copy()

# Split multiple countries into separate rows
country_data["country"] = country_data["country"].str.split(",")

country_data = country_data.explode("country")

# Remove extra spaces
country_data["country"] = country_data["country"].str.strip()

# Exclude empty country names
country_data = country_data[
    country_data["country"].notna()
    & (country_data["country"] != "")
].copy()

print("\nTotal country entries:", len(country_data))

# Step 3: Calculate country-wise content counts
country_counts = (
    country_data.groupby("country")
    .size()
    .sort_values(ascending=False)
)

# Exclude missing country labels from the ranking
country_counts = country_counts.drop(
    labels=["Not Given"], errors="ignore"
)

print("\nTOP 10 COUNTRIES BY CONTENT COUNT")
print(country_counts.head(10).to_string())


# Create a complete country ranking table
country_ranking = country_counts.reset_index()

country_ranking.columns = ["Country", "Content Count"]

country_ranking.insert(
    0,
    "Rank",
    range(1, len(country_ranking) + 1)
)

# Save country ranking to CSV
country_ranking.to_csv(
    "Task 3/Task3_Country_Ranking.csv",
    index=False
)

print("\nCountry ranking saved successfully.")
print(country_ranking.head(10).to_string(index=False))

import matplotlib.pyplot as plt

# Select the top 10 countries
top_10 = country_counts.head(10)

# Create a professional bar chart
plt.figure(figsize=(12, 7))

bars = plt.bar(
    top_10.index,
    top_10.values,
    color="#2878B5",
    edgecolor="white"
)

# Add content count labels above each bar
for bar in bars:
    count = int(bar.get_height())
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        count + 30,
        f"{count:,}",
        ha="center",
        va="bottom",
        fontsize=10,
        fontweight="bold"
    )

plt.title(
    "Top 10 Countries by Netflix Content",
    fontsize=16,
    fontweight="bold",
    pad=18
)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)
plt.xticks(rotation=35, ha="right")
plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

# Save the chart
plt.savefig(
    "Task 3/Task3_Top10_Countries.png",
    dpi=300,
    bbox_inches="tight"
)

print("Chart saved: Task3_Top10_Countries.png")

plt.show()
