# Import the heart failure prediction data set’s CSV file into a DataFrame.
import pandas as pd
df = pd.read_csv('heart.csv')

# Use shape to display the number of rows and columns of the DataFrame to the console window.
print(f'Shape of the dataframe:\n{df.shape}')

# Display the first 10 and last 20 rows of the dataset to the console window.
print(f'\nFirst 10 rows:\n{df.head(10)}\n\n Last 20 rows:\n {df.tail(20)}')

# Use describe() to display descriptive statistics for the dataset to the console window.
print(f'\nDescriptive statistics:\n{df.describe()}')

# Display the memory usage of each column in the data set to the console window without an index.
print(f'\nMemory usage without index:\n{df.memory_usage(index=False)}')

# Change the type of at least one of the columns in the dataset.
df['age'] = df['age'].fillna(0).astype(int)

# Ensure any duplicate rows are removed
df.drop_duplicates(keep=False, inplace= True)

# Save the contents of the DataFrame to a file called “updated_heart.csv”.
df.to_csv('updated_heart.csv', index=False)

# Generate the descriptive statistics for the dataset again and save these statistics to a file called “heart_statistics.csv”.
statistics_file = pd.DataFrame(df.describe())
statistics_file.to_csv('heart_statistics.csv', index=False)



























