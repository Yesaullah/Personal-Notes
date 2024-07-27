import pandas as pd

# reading data from the file
bios = pd.read_csv(r'D:\Python\Pandas\bios.csv')

# -------------------------------------
# SINGLE FILTERING CONDITION

# print(bios.loc[bios['height_cm'] > 220])
# print(bios[bios['height_cm'] > 220][['name', 'born_date']])
# -------------------------------------

# -------------------------------------
# MULTIPLE FILTERING CONDITION

# print(bios[(bios['height_cm'] > 215) & (bios['born_country'] == 'USA')])
# print(bios[bios['name'].str.startswith('Keith')])
# print(bios[bios['name'].str.contains("Patrick|Keith")]) # check for Keith or Patrick
# -------------------------------------

# -------------------------------------
# FILTERING USING QUERY FUNCTION

# print(bios.query('born_country == "GBR" or born_country == "USA"'))
# print(bios.query('height_cm > 215 and born_country == "USA" and weight_kg > 105'))
# print(bios.query('name.str.startswith("Keith")'))
max_height = 200
min_height = 190
# print(bios.query('height_cm > @min_height and height_cm < @max_height').sort_values("height_cm", ascending=False))