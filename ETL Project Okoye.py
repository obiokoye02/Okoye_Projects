# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 18:19:56 2023

@author: Travi
"""

import pandas as pd
import requests as r
import io

# Read in the CSV files for HR, Sales, and Item data
filepath = '/Users/Travi/Downloads/'
url = "http://drd.ba.ttu.edu/isqs3358/hw2/" 
files = ['hr_data.csv', 'sales_data.csv', 'Item_data.csv'] 
file_out = 'title_benefit_raises.csv'

res = r.get(url + files[0])
dfhr = pd.read_csv(io.StringIO(res.text), delimiter='|')

res = r.get(url + files[1])
dfsales = pd.read_csv(io.StringIO(res.text), delimiter=',')

res = r.get(url + files[2])
dfitem = pd.read_csv(io.StringIO(res.text), delimiter='|')

# Merge the datasets into a single dataset
dffinal = dfhr.merge(dfsales, how='inner', on='EmpId')
dffinal = dffinal.merge(dfitem, how='inner', left_on='VendorCode', right_on='VendorID')

# Handle missing values by computing column aggregates based on title
dfmissing = dffinal.groupby('Title').agg({
    'Salary': 'mean',
    'Benefits': 'mean',
    'ItemSold': 'mean',
    'SalesValue': 'mean'
}).reset_index()

# Rename the column headers
dfmissing.rename(columns={
    'Salary': 'Avg_Salary',
    'Benefits': 'Avg_Benefits',
    'ItemSold': 'Avg_ItemSold',
    'SalesValue': 'Avg_SalesValue'
}, inplace=True)

# Join the aggregated data back to the main dataframe
df = dffinal.merge(dfmissing, how='inner', on='Title')

# Calculate the new columns as requested
df['Per_Item_Benefit'] = df['Benefits'] / df['ItemSold']
df['Total_Compensation'] = df['Salary'] + df['Benefits']
df['Performance_metrics'] = df['Total_Compensation'] / (df['ItemSold'] / df['Avg_ItemSold'])

# Define employee_raise_elligible
def raise_eligibility(row):
    if row['Title'] == 'Sales Associate 1' and row['Performance_metrics'] > 238:
        return 'Yes'
    elif row['Title'] == 'Sales Associate 2' and row['Performance_metrics'] > 704:
        return 'Yes'
    elif row['Title'] == 'Sales Associate 3' and row['Performance_metrics'] > 938:
        return 'Yes'
    elif row['Title'] == 'Sales Manager' and row['Performance_metrics'] > 2146:
        return 'Yes'
    else:
        return 'No'

df['employee_raise_elligible'] = df.apply(raise_eligibility, axis=1)

# Calculate the average Total_Compensation, Per_Item_Sale, Performance_metrics by Title
title_aggregate = df.groupby('Title').agg({
    'Total_Compensation': 'mean',
    'Per_Item_Benefit': 'mean',
    'Performance_metrics': 'mean'
}).reset_index()

# Output to "title_aggregate.csv"
title_aggregate.to_csv('title_aggregate.csv', index=False)

# Create employees that will get a raise
employee_raise = df[df['employee_raise_elligible'] == 'Yes']
employee_raise.to_csv('employee_raise.csv', index=False)

# Define benefit raises based on job titles
benefit_raise = {
    'Sales Associate 1': 0.075,
    'Sales Associate 2': 0.07,
    'Sales Associate 3': 0.065,
    'Sales Manager': 0.06
}

# Calculate updated_benefit and benefit_diff
df['updated_benefit'] = df['Title'].map(benefit_raise)
df['benefit_diff'] = df['Benefits'] * df['updated_benefit']

# Compute the total_benefit, updated_benefit, benefit_diff by job title for employees getting a raise
title_benefit_raises = df[df['employee_raise_elligible'] == 'Yes'].groupby('Title').agg({
    'Benefits': 'sum',
    'updated_benefit': 'sum',
    'benefit_diff': 'sum'
}).reset_index()

# Output to "title_benefit_raises.csv"
title_benefit_raises.to_csv('title_benefit_raises.csv', index=False)