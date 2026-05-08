import pandas as pd

def detect_outliers_iqr(series: pd.Series) -> pd.Series:
    q1 = series.quantile(0.25)   #compute first quartile
    q3 = series.quantile(0.75)   #compute third quartile
    iqr = q3 - q1                #calculate the interquartile range
    lower_bound = q1 - 1.5 * iqr #set lower "typical" bound at 1.5 below q1
    upper_bound = q3 + 1.5 * iqr #set upper "typical" bound at 1.5 above q3
    return (series < lower_bound) | (series > upper_bound) #return a boolean mask indicating True for any value outside those bounds

# Example usage:
data = {
    "score": [10, 12, 13, 14, 15, 16, 17, 18, 100, 110]
}
df = pd.DataFrame(data)
outliers = detect_outliers_iqr(df["score"])
print(outliers)
