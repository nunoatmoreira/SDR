import pandas as pd
import numpy as np # if your arrays are NumPy arrays, otherwise just use lists

# 1. Define your two arrays (lists or NumPy arrays)
array_a = [10, 20, 30, 40, 50]
array_b = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']

# 2. Create a dictionary where keys are your desired column names
data = {'Column_A': array_a, 'Column_B': array_b}

# 3. Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# 4. Export the DataFrame to a CSV file
# index=False prevents writing the DataFrame index (0, 1, 2, ...) to the CSV
df.to_csv('output_pandas.csv', index=False)

print("File 'output_pandas.csv' created successfully using Pandas.")