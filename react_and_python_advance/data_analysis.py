import pandas as pd

# Load your data from a CSV file (replace 'data.csv' with your file path)
data = pd.read_csv("data.csv")

# Perform some data analysis, e.g., calculate the sum of a specific column
sum_of_column = data["ssc_p"].sum()

# Print the result (you can modify this to return data in a desired format)
print(sum_of_column)
