# This code converts all string values in a specified DataFrame column to lowercase.
import pandas as pd

def standardize_column_lowercase(df, column_name):
    model_df = df.copy()
    model_df[column_name] = model_df[column_name].str.lower()
    return model_df

data = {
    "fruit": ["Apple", "banana", "ORANGE", "apple", "Banana", "orange"],
    "quantity": [5, 3, 4, 2, 1, 6]
}
df = pd.DataFrame(data)
result = standardize_column_lowercase(df, "fruit")
print(result)
