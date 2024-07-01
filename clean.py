import pandas as pd
import sys

# Check if the required arguments are provided
if len(sys.argv) != 4:
    print("Usage: python clean.py <input1> <input2> <output>")
    sys.exit(1)

# Get the input and output file paths from the command-line arguments
input1 = sys.argv[1]
input2 = sys.argv[2]
output = sys.argv[3]

# Load the input data files
df1 = pd.read_csv(input1)
df2 = pd.read_csv(input2)

# Merge the data frames based on the ID value
df = pd.merge(df1, df2, left_on='respondent_id', right_on='id', how='inner')

# Drop rows with missing values
df = df.dropna()

# Drop rows where the job value contains 'insurance' or 'Insurance'
df = df[~df['job'].str.contains('insurance', case=False)]

# Save the cleaned data to the output file
df.to_csv(output, index=False)

print(f"Data cleaning completed. Output file saved at: {output}")