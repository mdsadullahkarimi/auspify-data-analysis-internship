
import pandas as pd

# Load the cleaned Netflix dataset
df = pd.read_csv("cleaned_netflix_data.csv")

print("NETFLIX BUSINESS INSIGHTS REPORT")
print("-" * 40)

print("Total Titles:", len(df))
print("Total Columns:", len(df.columns))

print("\nContent Type Distribution:")
print(df["type"].value_counts())

print("\nTop 5 Countries:")
countries = (
    df["country"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

countries = countries[countries != "Not Given"]
print(countries.value_counts().head(5))

print("\nTop 5 Genres:")
genres = (
    df["listed_in"]
    .dropna()
    .str.split(",")
    .explode()
    .str.strip()
)

print(genres.value_counts().head(5))

# ----------------------------------------
# BUSINESS INSIGHTS AND RECOMMENDATIONS
# ----------------------------------------

import os

# Create output folder path
output_file = "Task 6/Task6_Business_Insights.txt"

# Calculate content type percentages
type_counts = df["type"].value_counts()
total_titles = len(df)

movie_count = type_counts.get("Movie", 0)
tv_count = type_counts.get("TV Show", 0)

movie_pct = movie_count / total_titles * 100
tv_pct = tv_count / total_titles * 100

# Find top country and genre
top_country = countries.value_counts().index[0]
top_country_count = countries.value_counts().iloc[0]

top_genre = genres.value_counts().index[0]
top_genre_count = genres.value_counts().iloc[0]

# Build report
report = f"""
NETFLIX BUSINESS INSIGHTS REPORT
================================

1. DATASET OVERVIEW
Total titles analysed: {total_titles}
Total columns: {len(df.columns)}

2. CONTENT TYPE ANALYSIS
Movies: {movie_count} ({movie_pct:.2f}%)
TV Shows: {tv_count} ({tv_pct:.2f}%)

Insight:
Movies represent the larger share of the Netflix titles in this dataset.

3. COUNTRY ANALYSIS
Top country: {top_country}
Country title associations: {top_country_count}

Insight:
The United States has the highest number of country-title associations
in this dataset.

4. GENRE ANALYSIS
Top genre: {top_genre}
Genre title associations: {top_genre_count}

Insight:
{top_genre} is the most frequently listed genre in this dataset.

5. BUSINESS RECOMMENDATIONS
- Monitor the balance between Movies and TV Shows in the catalog.
- Review country and genre distributions when planning catalog analysis.
- Combine catalog data with viewership and engagement metrics before
  making audience-demand decisions.
- Use additional market and performance data to evaluate content strategy.

6. LIMITATIONS
- One title may be associated with multiple countries or genres.
- Title counts do not measure views, revenue, or audience preference.
- Findings describe this dataset and do not establish causal relationships.

================================
Report generated using Python and Pandas.
"""

# Save report
with open(output_file, "w", encoding="utf-8") as file:
    file.write(report)

print("\nBusiness insights report saved successfully:")
print(output_file)


import matplotlib.pyplot as plt

# Content type counts
type_counts = df["type"].value_counts()

# Create chart
plt.figure(figsize=(9, 6))
bars = plt.bar(
    type_counts.index,
    type_counts.values,
    edgecolor="black"
)

plt.title("Netflix Content Type Distribution", fontsize=15)
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.grid(axis="y", linestyle="--", alpha=0.4)

# Display values above bars
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{int(height):,}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# Save chart inside Task 6 folder
plt.savefig("Task 6/Task6_Content_Type_Chart.png", dpi=300)
print("Business insights chart saved successfully!")

plt.show()
