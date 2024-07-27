import pandas as pd
# --------------------------------------------------------------------------------------------------------------------
coffee = pd.read_csv(r'D:\Python\Pandas\coffee.csv')
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# print(coffee.sample(10)) # this will print data about 10 random entries
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
#  ACCESSING SPECIFIC ROWS AND COLUMNS

# -------------------------------------
# print(coffee.loc[1]) # this will return row with index 1 only
# print(coffee.loc[[1, 4, 6]]) # this way we can access specific rows
# print(coffee.loc[5:8]) # we can also make use of slicing 
# -------------------------------------

# -------------------------------------
# print(coffee.loc[5:8, "Day"]) # this will print the data from indexes 5 to 8 but only data in column 'Day'
# print(coffee.loc[4:7, ["Day", "Units Sold"]]) # this will print the data from indexes 4 to 7 but only data in column 'Day' and 'Units Sold'
# -------------------------------------

# -------------------------------------
# iloc() works in almost the same way as loc(), the only difference is that it takes int indexes for columns as well
# print(coffee.iloc[2:5, :]) # this will print the data in all the columns for row 2 to row 4
# print(coffee.iloc[:, [1, 2]])
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# WE CAN RENAME THE INDEXES OF THE DATAFRAME ACCORDING TO A COLUMNS DATA
# coffee.index = coffee["Day"]
# print(coffee.head())
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# MODIFYING DATA IN A DATAFRAME

# -------------------------------------
# changing data in a single cell
# print(coffee.loc[0:2])
# coffee.loc[1, "Units Sold"] = 69
# print(coffee.loc[0:2])
# -------------------------------------

# -------------------------------------
# changing data in multiple cells
# coffee.loc[1:3, "Coffee Type"] = "Mocha"
# print(coffee.head(5))
# -------------------------------------
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# ACCESSING A SINGLE CELL DATA

# using at(), this accepts string literal for columns
# print(coffee.at[0, "Coffee Type"])

# using iat(), this accepts integers for columns
# print(coffee.iat[3, 1])
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# ACCESSING A SINGLE COLUMN
# print(coffee["Units Sold"]) # single column
# print(coffee[2])
# --------------------------------------------------------------------------------------------------------------------

# --------------------------------------------------------------------------------------------------------------------
# ACCESSING A SPECIFIC COLUMNS AND SPECIFIC ROWS
# print(coffee[['Day', 'Units Sold']][0:5])
# --------------------------------------------------------------------------------------------------------------------
# SORTING THE DATA

# print(coffee.sort_values("Coffee Type"))
# print(coffee.sort_values(["Units Sold", "Coffee Type"]))