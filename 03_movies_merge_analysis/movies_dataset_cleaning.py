import pandas as pd

# Loading the .csv files into DataFrames
df_1 = pd.read_csv('movies_part_1.csv', delimiter=',')
df_2 = pd.read_csv('movies_part_2.csv', delimiter=',')
df_3 = pd.read_csv('movies_part_3.csv', delimiter=',')

# Append df_2 into df_1
df_1_2 = pd.concat([df_1, df_2])

# Adding columns from df_3 to df_1_2
df = pd.merge(df_1_2, df_3, how="left", on='id')

# Replacing all missing numeric values with the median of the column in which they're found
numeric_cols = ["popularity", "vote_average", "vote_count", "revenue", "runtime"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())


# Replacing all missing string values with the mode of the column in which they're found
df['original_language'] = df['original_language'].fillna(df['original_language'].mode()[0])
df['original_title'] = df['original_title'].fillna(df['original_title'].mode()[0])

# Sorting by release_date and popularity
df.sort_values(by=['release_date', 'popularity'], inplace=True)

# Output the mean revenue at vote_average
print(df.groupby(by='vote_average')['revenue'].mean())




