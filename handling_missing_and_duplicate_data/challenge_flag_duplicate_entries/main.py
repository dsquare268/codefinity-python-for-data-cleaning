# This code adds a boolean column 'is_duplicate to the dataframe
import pandas as pd

def flag_duplicates(df):
    df_copy = df.copy()
    df_copy['is_duplicate'] = df_copy.duplicated(keep=False)
    return df_copy

data = {
    "id": [1, 2, 2, 3, 4, 4, 4],
    "name": ["Alice", "Bob", "Bob", "Charlie", "David", "David", "David"],
    "score": [85, 90, 90, 95, 80, 80, 80]
}
df = pd.DataFrame(data)
result = flag_duplicates(df)
print(result)
