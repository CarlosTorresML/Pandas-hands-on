# 🎬 Movies Dataset – Merging and Analysis Task

This task focuses on data cleaning, merging, and exploratory analysis using the Pandas library. The dataset comes from the "Top 10000 Popular Movies" collection, split into three `.csv` files.

## 🎯 Objective

Combine and clean multiple movie-related datasets to generate a unified DataFrame and analyze movie revenue grouped by vote average.

## 🧪 What was done

- Loaded three `.csv` files into separate Pandas DataFrames
- Appended entries from `movies_part_2.csv` to the end of `movies_part_1.csv`
- Merged the resulting DataFrame with `movies_part_3.csv` (column-wise) using the movie ID
- Replaced all missing **numeric** values with the **median** of their respective columns
- Replaced all missing **string** values with the **most frequent value** (mode) of each column
- Sorted the full dataset by `release_date` and `popularity`
- Displayed the **mean revenue** for each unique `vote_average` score

## 🧰 Libraries used
- Pandas

## ▶️ How to run
- Make sure you have all three CSV files in the same directory and run:
---> python movies_merge_analysis.py

## 📊 Example output

```bash
vote_average
0.0     0.000000
1.0     25737.143
2.0     107118.391
...
