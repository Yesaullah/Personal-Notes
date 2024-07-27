import pandas as pd
import numpy as np

coffee = pd.read_csv(r'D:\Python\Pandas\coffee.csv')

# -------------------------------------
# ADDING A PRICE COLUMN
coffee['Price'] = np.where(coffee['Coffee Type']=='Espresso', 3.99, 5.99)

# print(coffee.head())
# -------------------------------------

# -------------------------------------
# FIRST WE WILL ADD A RANDOM COLUMN
coffee['Shop Name'] = "Costa"
# NOW WE NEED TO REMOVE THIS COLUMN
coffee.drop(columns=['Shop Name'], inplace=True)
# print(coffee.head())
# -------------------------------------

# -------------------------------------
# Shallow copy and Deep copy concept
new_coffee = coffee
# new_coffee.drop(columns=['Price'], inplace=True) # This is shallow copy, new_coffee points to the same memory as coffee

# coffee_deepCopy = coffee.copy()
# coffee_deepCopy.drop(columns=['Price'], inplace=True)
# print(coffee.head(2))
# print(coffee_deepCopy.head(2))
# -------------------------------------

# -------------------------------------
# ADDING A COLUMN BY IMPLEMENTING A MATHEMATICAL FUNCTION ON COLUMNS
coffee['Revenue'] = coffee['Price'] * coffee['Units Sold']
# print(coffee.head())
# -------------------------------------

# -------------------------------------
# RENAMING COLUMNS
coffee.rename(columns={
    'Day' : 'day', 
    'Coffee Type' : 'coffee type', 
    'Units Sold' : 'units sold', 
    'Price' : 'price', 
    'Revenue' : 'revenue'  
}, inplace=True)
# print(coffee.head())
# -------------------------------------

# -------------------------------------
bios = pd.read_csv(r'D:\Python\Pandas\bios.csv')

# bios_new = bios.copy()

# -------------------------------------

# ADDING A NEW COLUMN USING THE EXISTING COLUMN
# bios_new['first_name'] = bios_new['name'].str.split(' ').str[0]

# -------------------------------------

# -------------------------------------

# bios_new['DoB'] = pd.to_datetime(bios_new['born_date'], format="%Y-%m-%d")

# bios_new['born_year'] = bios_new['DoB'].dt.year

# CREATING A CSV FILE FROM THE DATAFRAME
# bios_new.to_csv('./Pandas/bios_new.csv', index=False)
# -------------------------------------

# -------------------------------------
# ADDING A NEW COLUMN USING APPLY() AND LAMBDA FUNCTION
bios['height_category'] = bios['height_cm'].apply(lambda x: 'Short' if x < 165 else ('Average' if x < 185 else 'Tall'))

# print(bios.head(3))
