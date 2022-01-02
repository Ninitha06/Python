import pandas as pd


df = pd.DataFrame({'id' : ['RU','IN','CH'],'country':['Russia', 'India', 'China'], 
'capital':['Moscow','New Delhi','Beijing'], 
'area':[17.100,3.286,9.597],   
'population' : [143.50,1252.00,1357.00]})


df.set_index('id', inplace=True)


# print(df)

# print(df["country"])

# print(type(df["country"]))

# print(df[["country"]])

# print(type(df[["country"]]))

# print(df[["country", "capital"]])

# Rows - last index is exclusive
# print(df[1:3])


# print(df.loc["RU"])

# print(df.loc[["RU", "IN", "CH"]])

# print(df.loc[["RU", "IN", "CH"], ["country", "capital"]])


print(df.loc[:, ["country", "capital"]])

#  Row and columns
print(df.iloc[[1, 2]])

print(df.iloc[[1, 2], [0, 1]])

