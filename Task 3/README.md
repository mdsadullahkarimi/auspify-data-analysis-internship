# Task 3: Country-Wise Netflix Content Analysis

## Project Overview
This project analyzes the country-wise distribution of Netflix content using Python. It identifies the countries with the highest number of titles and presents the results through a ranking table and bar chart.

## Objectives
- Extract and clean country information.
- Calculate content counts for each country.
- Identify the top 10 countries by content count.
- Create a bar chart and country ranking table.
- Generate business insights from the analysis.

## Tools and Technologies
- Python
- Pandas
- Matplotlib

## Project Files
- `Task3.py` — Python source code for the analysis.
- `Task3_Top10_Countries.png` — Bar chart of the top 10 countries.
- `Task3_Country_Ranking.csv` — Complete country-wise ranking table.
- `Task3_Business_Insights.txt` — Business insights and conclusion.

## Key Findings
- United States: 3,240 title-country associations.
- India: 1,057 title-country associations.
- United Kingdom: 638 title-country associations.

The United States ranks first, followed by India and the United Kingdom.

**Note:** A single Netflix title may be associated with multiple countries. Therefore, country counts represent title-country associations and should not be interpreted as unique titles.

## How to Run the Project
Run the following command from the main project folder:

```bash
python "Task 3/Task3.py"
```

Ensure that `cleaned_netflix_data.csv` is available in the main project folder and the required Python libraries are installed.

## Conclusion
This analysis provides a country-wise view of Netflix content and helps identify the countries most strongly represented in the dataset.