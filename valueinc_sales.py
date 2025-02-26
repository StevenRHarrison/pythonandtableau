#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:22:23 2024

@author: stevenharrison
"""

#     IMPORTS

import pandas as pd

# file_name = pd.read_csv('file.csv')   <--- format of read_csv

# data = pd.read_csv('transaction2.csv') 

data = pd.read_csv('transaction.csv', sep=';')

# summary of the data

data.info()


# Working with calculations

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased * CostPerItem
SellingPricePerTransaction = NumberOfItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation

# CostPerTransacction = CostPerItem * NumberOfItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# adding a new column to a dataframe

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation

data['Profit'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup  = (Sales-Cost)/cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']
# data['Markup1'] = (data['Profit']) / data['CostPerTransaction']


# Rounding Markup Function

roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'],2)

# Combining Data Fields - Concatenate

my_date = 'Day'+'-'+'Month'+'-'+'Year'

# my_date = data['Day']+'-'


# Change Columns data type
print(data['Day'].dtype)

#change cloumns type

day = data['Day'].astype(str)
year = data['Year'].astype(str)

print(day.dtype)
print(year.dtype)

my_date =  day+'-'+data['Month']+'-'+year
data['date'] = my_date

# using iloc to view specific columns and rows

data.iloc[0:3]  # first 3 rows
data.iloc[-5:]  # last 5 rows
data.iloc[5:]   # last 5 rows

data.iloc[:,2]  # all rows on the 2nd column
data.iloc[4,2]  # brings in 4th row, 2nd column


#  using split to split the lient keywords field
#  new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)

# creating new columns for the split columns in Client Keywords

data['Client_Age'] = split_col[0]
data['Client_Type'] = split_col[1]
data['Client_Length_of_Contract'] = split_col[2]
          
# using the replace function

data['Client_Age'] = data['Client_Age'].str.replace('[' , '')
data['Client_Length_of_Contract'] = data['Client_Length_of_Contract'].str.replace(']' , '')

data['Client_Age'] = data['Client_Age'].str.replace('\'' , '')
data['Client_Type'] = data['Client_Type'].str.replace('\'' , '')
data['Client_Length_of_Contract'] = data['Client_Length_of_Contract'].str.replace('\'' , '')

# using the lower function to change item to lowercase

data['ItemDescription'] = data['ItemDescription'].str.lower()

# how to merge files

# bringing in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# merging files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

# dropping columns
# df = df.drop('columnename' , axis = 1)

data = data.drop(['Day'], axis = 1)
data = data.drop(['Month','Year'], axis = 1)

# Export into a CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)
















































