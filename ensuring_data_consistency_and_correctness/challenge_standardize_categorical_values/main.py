import pandas as pd

def standardize_column_case(df, column_name):#define function that accepts DataFrame(df) and the name of a column
    model_df = df.copy()
    #makes a copy of the input dataframe so the original isn't modified in-place
    model_df[column_name] = model_df[column_name].str.lower() 
    #Converts every string in the specified column to lowercase using pandas’ string methods.
    return model_df #Returns the new, lowercase-standardized DataFrame.

data = {
    "Response": ["Yes", "no", "YES", "No", "yes", "NO", "nO", "YeS"]
}
df = pd.DataFrame(data)
#Builds a sample DataFrame with mixed-case “Yes”/“No” responses.
result = standardize_column_case(df, "Response")
#Calls your function on that DataFrame, standardizing the “Response” column.
print(result)
#Shows the modified DataFrame, where all entries in “Response” are now lowercase.