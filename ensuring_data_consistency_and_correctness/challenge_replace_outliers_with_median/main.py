import pandas as pd

def replace_outliers_with_median(df, column, outlier_mask):
    median_value = df.loc[~outlier_mask, column].median() #computes the median of all values in column where outlier_mask is False (i.e. non-outliers)
    df.loc[outlier_mask, column] = median_value           #replaces every outlier in that colunn (where outlier_mask is True) with the computed median.
    return df   #return the modified dataframe.

# Example usage
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "score": [85, 90, 300, 88, 92]
}
df = pd.DataFrame(data)
outlier_mask = df["score"] > 150  # created outlier_mask by marking scores > 150 as True.

replace_outliers_with_median(df, "score", outlier_mask)
print(df)
