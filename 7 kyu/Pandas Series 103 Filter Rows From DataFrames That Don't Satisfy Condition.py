```
Filter Rows From DataFrames That Don't Satisfy Condition
Input parameters
dataframe: pandas.DataFrame object
col: target column
func: filter function
Task
Your function must return a new pandas.DataFrame object with the same columns as the original input. However, include only the rows whose cell values in the designated column evaluate to False by func.
Input DataFrame will never be empty. The target column will always be one of the dataframe columns. Filter function will be a valid one. Index value must remain the same.
Examples
Input
   A  B  C
0  1  2  3
1  4  5  6
2  6  3  2
3  1  1  7
col = "A"
func = lambda x: x<=2
Output
   A  B  C
1  4  5  6
2  6  3  2
```

import pandas as pd

def filter_dataframe(dataframe: object, col: str, func): 
    filter_mask = dataframe[col].apply(func)
    filtered_df = dataframe.loc[~filter_mask]
    return filtered_df