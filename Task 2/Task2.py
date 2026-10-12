import pandas as pd
df =pd.read_csv("cleaned_netflix_data.csv")
print(df.head())
print(df.shape)
print(df["type"].value_counts(normalize=True)*100)

import matplotlib.pyplot as plt

content_counts = df["type"].value_counts()
percentages = content_counts / content_counts.sum() * 100

fig, ax = plt.subplots(figsize=(9, 6))

bars = ax.bar(
    content_counts.index,
    content_counts.values,
    color=["#E50914", "#564D4D"],
    width=0.6
)

ax.set_title(
    "Netflix Content Distribution",
    fontsize=18,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Content Type", fontsize=12)
ax.set_ylabel("Number of Titles", fontsize=12)

ax.set_ylim(0, content_counts.max() * 1.18)
ax.grid(axis="y", linestyle="--", alpha=0.3)
ax.set_axisbelow(True)

for i, bar in enumerate(bars):
    count = content_counts.iloc[i]
    percentage = percentages.iloc[i]

    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 80,
        f"{count:,}\n({percentage:.2f}%)",
        ha="center",
        va="bottom",
        fontsize=12,
        fontweight="bold"
    )

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.savefig(
    "Task2_Content_Type_Chart.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
total_titles = content_counts.sum()

movie_count = content_counts.get("Movie", 0)
tv_count = content_counts.get("TV Show", 0)

movie_percentage = movie_count / total_titles * 100
tv_percentage = tv_count / total_titles * 100

with open("Task2_Summary_Report.txt", "w") as file:
    file.write("NETFLIX CONTENT TYPE ANALYSIS\n")
    file.write("=" * 35 + "\n\n")

    file.write(f"Total titles: {total_titles}\n")
    file.write(f"Movies: {movie_count}\n")
    file.write(f"TV Shows: {tv_count}\n\n")

    file.write(f"Movie percentage: {movie_percentage:.2f}%\n")
    file.write(f"TV Show percentage: {tv_percentage:.2f}%\n\n")

    file.write("KEY FINDINGS\n")
    file.write("Movies make up the majority of Netflix titles.\n")
    file.write("Movies account for 69.69% of the dataset.\n")
    file.write("TV Shows account for 30.31% of the dataset.\n")

print("Summary report saved successfully.")