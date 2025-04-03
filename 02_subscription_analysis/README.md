# 🧾 Subscription Revenue Analysis

This task simulates a real-world data cleaning and analysis process using the Pandas library. The dataset contains information about users, their subscription type, payment amounts, and join dates.

## 🎯 Objective

Clean and analyze a dataset of platform subscriptions to determine:

- Total revenue per subscription type
- Users who pay more than 10€
- Duplicate users
- Handling of missing values

## 🧪 What was done

- Loaded the data into a Pandas DataFrame
- Converted `join_date` column to datetime
- Removed duplicate users based on `user_id`
- Replaced missing values:
  - `payment_amount` → 0
  - `subscription_type` → "Unknown"
- Created a new column: `monthly_income`
- Grouped and summarized total income by subscription type
- Filtered users who pay more than 10€
- Saved the cleaned dataset to `clean_subscriptions.csv`

## 🧰 Tools used

- Python 3.x
- Pandas

