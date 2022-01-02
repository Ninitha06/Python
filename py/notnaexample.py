
# importing pandas as pd
import pandas as pd
 
# Creating the first dataframe
df = pd.DataFrame({"A":[14, 4, 5, 4, 1],
                   "B":[5, 2, None, None, 2],
                   "C":[20, 20, 7, 3, 8],
                   "D":[14, 3, 6, 2, 6]})
 
# Print the dataframe
print(df)

print(df.notna())

df = df[df["B"].notna()]

print(df)