# Heart Failure Dataset – Data Cleaning Task

This task involves working with the Heart Failure Prediction dataset using the Pandas library in Python. The objective is to perform a basic but complete data cleaning and inspection workflow, including type conversion, duplicate removal, memory usage analysis, and exporting results.

## 🔧 What was done

- Loaded the dataset from `heart.csv` into a Pandas DataFrame.
- Displayed dataset shape, first 10 rows, and last 20 rows.
- Generated descriptive statistics using `.describe()`.
- Analyzed memory usage per column using `.memory_usage(index=False)`.
- Converted the data type of the `age` column from float to integer.
- Removed all duplicate rows using `.drop_duplicates()`.
- Saved the cleaned dataset to `updated_heart.csv`.
- Saved the updated descriptive statistics to `heart_statistics.csv`.

## 📁 Files included

- `heart.csv`: Original dataset (input file)
- `clean_heart_data.py`: Python script with all cleaning steps
- `updated_heart.csv`: Cleaned and deduplicated dataset
- `heart_statistics.csv`: Descriptive statistics of the cleaned data
- `README.md`: This documentation file

## ▶️ How to run

Open a terminal in this folder and run:

```bash
python clean_heart_data.py
