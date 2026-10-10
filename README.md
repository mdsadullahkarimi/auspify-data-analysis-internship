# Netflix Data Cleaning and Preparation

## Project Overview
This project focuses on cleaning and preparing the Netflix Movies and TV Shows dataset using Python and Pandas.

## Objectives
- Load and inspect the Netflix dataset.
- Identify missing values.
- Detect and remove duplicate rows.
- Remove extra spaces from text columns.
- Standardize content type and rating values.
- Handle missing values in selected columns.
- Convert `date_added` to datetime format.
- Export the cleaned dataset to CSV.

## Tools Used
- Python
- Pandas
- Visual Studio Code

## Files
- `Dataset.csv` — Original dataset.
- `Task1.py` — Python source code.
- `cleaned_netflix_data.csv` — Cleaned dataset.

## Data Cleaning Process
1. Imported the dataset using Pandas.
2. Inspected rows, columns, data types, and missing values.
3. Removed duplicate records.
4. Trimmed extra spaces from text columns.
5. Standardized the `type` and `rating` values.
6. Replaced missing values in selected text columns with `Unknown`.
7. Converted `date_added` to datetime format.
8. Exported the cleaned dataset to CSV.

## Output
The cleaned dataset is saved as `cleaned_netflix_data.csv`.

## Verification
The exported dataset should be checked for duplicate rows, missing values, and correct data types before submission.