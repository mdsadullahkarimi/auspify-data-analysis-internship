
# ============================================================
# PROJECT: Netflix Data Cleaning and Preparation
# TASK 1: Data Analysis Using Python Internship
# TOOLS: Python and Pandas
# ============================================================


# STEP 1: Import the Pandas library
# Pandas is used for loading, cleaning, and analyzing data.

import pandas as pd


print("=" * 60)
print("NETFLIX DATA CLEANING AND PREPARATION")
print("=" * 60)


# STEP 2: Check the Pandas version

print("\nSTEP 2: Pandas Version")
print("Pandas version:", pd.__version__)


# STEP 3: Load the original Netflix dataset
# Dataset.csv must be in the same folder as this Python file.

df = pd.read_csv("Dataset.csv")

print("\nSTEP 3: Dataset Loaded Successfully")


# STEP 4: Inspect the original dataset
# head() displays the first five rows.
# shape returns the number of rows and columns.
# info() displays column names, data types, and non-null counts.

print("\nSTEP 4: Original Dataset Overview")

print("\nFirst 5 rows:")
print(df.head())

print("\nOriginal dataset shape:", df.shape)

print("\nDataset information:")
df.info()


# STEP 5: Check missing values before cleaning
# isnull().sum() counts missing values in each column.

print("\nSTEP 5: Missing Values Before Cleaning")
print(df.isnull().sum())


# STEP 6: Check and remove duplicate rows
# duplicated().sum() counts duplicate rows.
# drop_duplicates() removes duplicate rows.

print("\nSTEP 6: Duplicate Records")

print("Duplicate rows before cleaning:", df.duplicated().sum())

df = df.drop_duplicates()

print("Duplicate rows after cleaning:", df.duplicated().sum())


# STEP 7: Clean extra spaces from text columns
# strip() removes spaces from the beginning and end
# of text values in object-type columns.

print("\nSTEP 7: Text Formatting")

text_columns = df.select_dtypes(include=["object", "str"]).columns

for col in text_columns:
    df[col] = df[col].str.strip()

print("Extra spaces removed from text columns.")


# STEP 8: Standardize the Type column
# title() standardizes capitalization.
# The replacement ensures "TV Show" uses consistent formatting.

print("\nSTEP 8: Standardizing Content Types")

if "type" in df.columns:
    df["type"] = df["type"].str.title()
    df["type"] = df["type"].replace("Tv Show", "TV Show")

    print("Content types after standardization:")
    print(df["type"].value_counts())


# STEP 9: Standardize the Rating column
# Uppercase formatting makes rating labels consistent.

print("\nSTEP 9: Standardizing Ratings")

if "rating" in df.columns:
    df["rating"] = df["rating"].str.upper()

    print("Rating values:")
    print(df["rating"].value_counts(dropna=False))


# STEP 10: Explore the Country column
# Display the ten most frequent country entries.
# Note: some rows may contain multiple countries in one cell.

print("\nSTEP 10: Country Analysis")

if "country" in df.columns:
    print("Top 10 country entries:")
    print(df["country"].value_counts().head(10))


# STEP 11: Handle missing values in selected text columns
# Missing values in these columns are replaced with "Unknown".
# This preserves the rows instead of deleting them.

print("\nSTEP 11: Handling Missing Values")

columns_to_fill = [
    "director",
    "cast",
    "country",
    "rating",
    "duration",
    "listed_in",
    "description"
]

for col in columns_to_fill:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

print("Missing values handled in selected text columns.")


# STEP 12: Convert date_added to datetime format
# errors="coerce" converts invalid or missing dates to NaT.
# NaT means a missing datetime value.

print("\nSTEP 12: Date Formatting")

if "date_added" in df.columns:
    df["date_added"] = pd.to_datetime(
        df["date_added"],
        errors="coerce"
    )

    print("Date data type:", df["date_added"].dtype)
    print(
        "Missing or invalid dates:",
        df["date_added"].isnull().sum()
    )


# STEP 13: Final data quality check
# Check the cleaned dataset's size, duplicates,
# missing values, and first five records.

print("\nSTEP 13: Final Data Quality Check")

print("Final dataset shape:", df.shape)

print("Remaining duplicate rows:", df.duplicated().sum())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nFirst 5 cleaned records:")
print(df.head())


# STEP 14: Export the cleaned dataset
# index=False prevents Pandas from adding an extra index column.
# The original Dataset.csv file remains unchanged.

output_file = "cleaned_netflix_data.csv"

df.to_csv(output_file, index=False)

print("\nSTEP 14: Dataset Exported Successfully")
print("Output file:", output_file)


# STEP 15: Verify the exported CSV
# Reload the saved file to confirm that it can be read.
# The date column is parsed again for accurate date verification.

print("\nSTEP 15: Verifying Exported Dataset")

cleaned_df = pd.read_csv(
    output_file,
    parse_dates=["date_added"]
    if "date_added" in df.columns
    else None
)

print("Exported dataset shape:", cleaned_df.shape)

print(
    "Duplicate rows in exported dataset:",
    cleaned_df.duplicated().sum()
)

print("\nMissing values in exported dataset:")
print(cleaned_df.isnull().sum())

print("\nExported dataset data types:")
print(cleaned_df.dtypes)

print("\nFirst 5 exported records:")
print(cleaned_df.head())


# STEP 16: Finish the project

print("\n" + "=" * 60)
print("TASK 1 DATA CLEANING COMPLETED")
print("Please review the final quality-check results.")
print("=" * 60)
