'''
Data Wrangling: Data Preprocessing: Data cleaning
making the data ready for the analysis

Data is available here:
https://github.com/swapnilsaurav/dataset

Dataset 1: hotel_bookings.csv
https://github.com/swapnilsaurav/Dataset/blob/master/hotel_bookings.csv

'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
df_link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/hotel_bookings.csv"
df = pd.read_csv(df_link)
print("Dataframe: ",df)
print("top 5 rows:\n",df.head())
print("last 3 rows:\n",df. tail(3))
print("numbers of rows and columns : ",df.shape)
print("total rows: ",df.shape[0])
print("Different colum types :\n",df.info())
print("Basic statistics:\n ",df.describe)
print("checking for missing values: ")
print(df.isnull().sum())

# plotting heatmap to visualize the missing values in each row and column
sns.heatmap(data=df.isnull(), cmap=sns.color_palette(['#07f045', '#f05507']))
#plt.show()


'''
How to handle missing values:
1. Remove them (delete rows and columns with missing values)
    if a specific column or row has more than 80% missing data- we delete them
2. Replace the missing values with Mean/Median (numerical columns) and Mode for non-numeric cols
3. Replace the missing values with bfill (backward fill) and ffill (Forward fill)
4. Replace the missing values with specific value (eg -9999 for numeric, "Not Available" for non-numeric
'''
col_to_delete = []
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())*100
    print(f"{col} has {pct_missing:.3f}% missing values")
    if pct_missing>80:
        print(f"{col} needs to be dropped")
        col_to_delete.append(col)

print("Columns to be deleted: ",col_to_delete)
print("Dropping the column(s) now")
df = df.drop(col_to_delete,axis=1) #axis=1 indicates list of column (0 is for rows)
print("2) Number of rows and columns: ",df.shape)

print('''Go through each column and see if it has missing values,
 if yes then create duplicate column with missing values''')
cols_with_missing_vals = []
for col in df.columns:
    pct_missing = np.mean(df[col].isnull())*100
    missing = df[col].isnull()
    if pct_missing>0:
        df[f'{col}_Missing'] =  missing
        cols_with_missing_vals.append(f'{col}_Missing')
print("New columns added: ",cols_with_missing_vals)
print("Now adding one more column to read the total number of missing values")
df["Total_Missing"] = df[cols_with_missing_vals].sum(axis=1)
print("Lenght of new columns = ",len(cols_with_missing_vals))
print("3. Shape of the dataset: ",df.shape)

df['Total_Missing'].value_counts().sort_index().plot.bar(x='index',y='Total_Missing')
#plt.show()
idx_to_delete = df[df['Total_Missing'] >20].index
print("Indices to be deleted: ",idx_to_delete)

df = df.drop(idx_to_delete,axis=0) #axis=0 indicates list of row
print("4) Number of rows and columns: ",df.shape)
# add the total missing column as well
cols_with_missing_vals.append('Total_Missing')
df = df.drop(cols_with_missing_vals,axis=1)
print("5) Number of rows and columns: ",df.shape)

# Now we have the processed data with the columns and rows removed which has many missing values

'''
Now we will focus on replacing the missing values
2. Replace the missing values with Mean/Median (numerical columns) and Mode for non-numeric cols
3. Replace the missing values with bfill (backward fill) and ffill (Forward fill)
4. Replace the missing values with specific value (eg -9999 for numeric, "Not Available" for non-numeric
option = 1 for mean/median/mode
        =2 for bfill/ffill
        =3 for specific values
'''
option = 2

# replace the missing values
list_numerical_cols = df.select_dtypes(include=[np.number])
list_object_cols = df.select_dtypes(exclude=[np.number])

for col in df.columns:
    pct_missing = np.mean(df[col].isnull())*100
    if pct_missing>0:
        if option==1: #mean/median mode
            if col in list_numerical_cols:
                med = df[col].median()
                df[col]=df[col].fillna(med)
    if col in list_object_cols:
                md = df[col].describe()['top']
                df[col]=df[col].fillna(md)
    if option==2:  # bfill/ffill
        if col in list_numerical_cols:
            df[col]=df[col].ffill()
    if col in list_object_cols:
        df[col]=df[col].bfill()
    if option==3: #specific values
        if col in list_numerical_cols:
            df[col]=df[col].fillna(-9999)
        if col in list_object_cols:
           df[col]=df[col].fillna("Not Available")

print("Final Checking for missing values: ")
print(df.isnull().sum())
