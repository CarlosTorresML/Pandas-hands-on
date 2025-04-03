import pandas as pd
import numpy as np

data = {
    'user_id': [101, 102, 103, 104, 105, 106, 102, 107, 108, 109, 110],
    'subscription_type': ['Premium', 'Basic', 'Premium', 'Basic', 'Free', 'Basic', 'Basic', 'Premium', 'Premium', np.nan, 'Free'],
    'payment_amount': [29.99, 9.99, 29.99, np.nan, 0, 9.99, 9.99, 29.99, np.nan, 0, 0],
    'join_date': ['2023-01-01', '2023-01-02', '2023-01-02', '2023-01-05', '2023-01-06',
                  '2023-01-06', '2023-01-02', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10']
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Converting join_date to datetime format
df['join_date'] = pd.to_datetime(df['join_date'])

# Deleting duplicate rows using user_id
df.drop_duplicates(subset='user_id', keep='first', inplace=True)

# Filling NaN values in payment_amount with 0
df['payment_amount'] = df['payment_amount'].fillna(0)

# Filling NaN values in subscription_type with 'Unknown'
df['subscription_type'] = df['subscription_type'].fillna('Unknown')

# Creating a new column 'monthly_income'
df['monthly_income'] = df['payment_amount']

# Showing total income by subscription_type
print(df.groupby(by='subscription_type')['payment_amount'].sum())

# Showing users that pay more than 10€
filter = df['payment_amount'] > 10
print(f'Users that pay more than 10€:\n{df[filter]}')

# Saving the DF into a .csv file
df.to_csv('clean_subscriptions.csv', index=False)
