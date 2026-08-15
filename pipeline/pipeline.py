import sys
import pandas as pd

if len(sys.argv) != 2:
    print("invalid number of arguments passed")
    sys.exit(1)

day = int(sys.argv[1])
print(f"Running pipeline for day: {day}")

df = pd.DataFrame(data={
    "A": [1, 2],
    "B": [3, 4]
})

print(df.head())

df.to_parquet(f"output_day_{day}.parquet")