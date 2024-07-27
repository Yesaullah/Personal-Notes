import pandas as pd

dataframe = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["A", "B", "C"], index=["X", "Y", "Z"])

# USING HEAD(), WE CAN VIEW THE DATA STARTING FROM THE TOP
# print(dataframe.head()) #t this can be used to view the first few rows of data
# print(dataframe.head(1)) # this will print the first row only
# print(dataframe.head(2)) # this will print the first two rows

# USING TAIL(), WE CAN VIEW THE DATA STARTING FROM THE END
# print(dataframe.tail()) # this will print the last few rows of data
# print(dataframe.tail(1)) # this will print the last row only
# print(dataframe.tail(2)) # this will print the last two rows

# JUST TO VIEW THE HEADERS OF THE COLUMNS WE CAN USE columns()
# print(dataframe.column)

# JUST TO VIEW THE INDEXES OF THE ROWS WE CAN USE index()
# print(dataframe.index.tolist())

# TO VIEW INFORMATION REGARDING THE DATA STORED IN A DATAFRAME WE CAN USE info()
# print(dataframe.info())

# TO VIEW SOME STATISTICAL INFORMATION ABOUT OUR DATA WE CAN USE describe()
# print(dataframe.describe())

# THIS RETURNS THE NUMBER OF UNIQUE VALUES IN EACH COLUMN
# print(dataframe.nunique())
# print(dataframe['B'].unique()) # this returns all the unique values in a specific column

# print(dataframe.shape) # this returns the shape of our dataframe

# print(dataframe.size) # this returns the number of elements in the dataframes