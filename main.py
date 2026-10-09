
import pandas as pd

# --- Parameters ---

run = '2'

# --- Begin code ---

path = './runs/Slop Run ' + run + '.csv'

df = pd.read_csv(path, sep=',')
columns = df.columns.to_list()

print(columns)

print(df.head(5))
