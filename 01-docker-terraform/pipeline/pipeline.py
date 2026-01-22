import sys
import pandas as pd

print(sys.argv)

# Receives the 1st parameter
month = int(sys.argv[1])
print(f'Hello pipeline, month {month}')

df = pd.DataFrame({"day": [1, 2], "num_passangers": [3, 4]})
df['month'] = month

print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")

