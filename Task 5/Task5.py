
import pandas as pd

# Load the cleaned Netflix dataset
df = pd.read_csv("cleaned_netflix_data.csv")

# Check dataset dimensions
print("Dataset Shape:", df.shape)

# Check column names
print("\nColumn Names:")
print(df.columns.tolist())

# Check first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Check missing values in rating and genre columns
print("\nMissing Values:")
for col in ["rating", "listed_in"]:
    if col in df.columns:
        print(f"{col}: {df[col].isnull().sum()}")

        
# ---------------------------------
# Task 5: Content Rating Analysis
# ---------------------------------

# Count content by rating
rating_counts = df["rating"].value_counts()

print("\nContent Rating Analysis:")
print(rating_counts)

# Save rating analysis to CSV
rating_counts.to_csv("Task 5/Task5_Rating_Analysis.csv", header=["Count"])

print("\nRating analysis saved successfully!")

import matplotlib.pyplot as plt

# Create a bar chart
plt.figure(figsize=(12, 6))

rating_counts.sort_values(ascending=False).plot(
    kind="bar",
    edgecolor="black"
)

plt.title("Netflix Content Rating Analysis")
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
plt.savefig("Task 5/Task5_Rating_Analysis.png", dpi=300)

plt.show()

print("Rating chart saved successfully!")


# Compare ratings by content type
rating_by_type = pd.crosstab(df["rating"], df["type"])

print("\nRating by Content Type:")
print(rating_by_type)

# Save comparison
rating_by_type.to_csv("Task 5/Task5_Rating_by_Type.csv")

# Create a stacked bar chart
rating_by_type.plot(
    kind="bar",
    stacked=True,
    figsize=(12, 6)
)

plt.title("Content Rating by Type: Movies vs TV Shows")
plt.xlabel("Content Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.legend(title="Content Type")
plt.tight_layout()

plt.savefig("Task 5/Task5_Rating_by_Type.png", dpi=300)
plt.show()

print("Rating-by-type analysis saved successfully!")

# Genre Analysis
genre_counts = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)

genre_counts = genre_counts[genre_counts != ""].value_counts()

top_10_genres = genre_counts.head(10)

print("\nTop 10 Netflix Genres:")
print(top_10_genres)

# Save genre analysis
top_10_genres.to_csv(
    "Task 5/Task5_Top10_Genres.csv",
    header=["Title Count"]
)

# Plot top 10 genres
plt.figure(figsize=(12, 6))
top_10_genres.sort_values().plot(
    kind="barh",
    edgecolor="black"
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")
plt.tight_layout()

plt.savefig("Task 5/Task5_Top10_Genres.png", dpi=300)
plt.show()

print("Genre analysis saved successfully!")


# Genre and Rating Analysis

genre_rating_df = df[["rating", "listed_in"]].copy()

# Split multiple genres into separate rows
genre_rating_df["listed_in"] = (
    genre_rating_df["listed_in"].str.split(",")
)

genre_rating_df = genre_rating_df.explode("listed_in")

# Reset index to avoid duplicate index labels
genre_rating_df = genre_rating_df.reset_index(drop=True)

# Clean genre names
genre_rating_df["listed_in"] = (
    genre_rating_df["listed_in"].str.strip()
)

# Remove empty genre values
genre_rating_df = genre_rating_df[
    genre_rating_df["listed_in"] != ""
]

# Count titles by genre and rating
genre_rating_counts = pd.crosstab(
    genre_rating_df["listed_in"],
    genre_rating_df["rating"]
)

print("\nGenre-wise Rating Analysis:")
print(genre_rating_counts.head(10))

# Save complete analysis
genre_rating_counts.to_csv(
    "Task 5/Task5_Genre_Rating_Analysis.csv"
)

print("\nGenre-wise rating analysis saved successfully!")
