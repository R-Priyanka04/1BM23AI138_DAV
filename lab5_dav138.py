#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv('lab5.csv')


pivot_revenue_by_date_salesperson = df.pivot_table(
    index='Date',
    columns='Salesperson',
    values='Revenue',
    aggfunc='sum'
)

print(pivot_revenue_by_date_salesperson)


average_revenue_per_product = df.groupby('Product')['Revenue'].mean()

print(average_revenue_per_product)

max_units_sold_by_salesperson = df.groupby('Salesperson')['Units Sold'].max()

print(max_units_sold_by_salesperson)

total_revenue = df['Revenue'].sum()
revenue_by_region = df.groupby('Region')['Revenue'].sum()
percentage_revenue_by_region = (revenue_by_region / total_revenue) * 100

print(percentage_revenue_by_region)

sales_count_by_salesperson = df.groupby('Salesperson').size()
most_transactions_salesperson = sales_count_by_salesperson.idxmax()

print(most_transactions_salesperson)
print(sales_count_by_salesperson)

pivot_revenue_units_by_salesperson_product = df.pivot_table(
    index='Salesperson',
    columns='Product',
    values=['Revenue', 'Units Sold'],
    aggfunc='sum'
)

print(pivot_revenue_units_by_salesperson_product)

pivot_units_by_date_region = df.pivot_table(
    index='Date',
    columns='Region',
    values='Units Sold',
    aggfunc='sum'
)

print(pivot_units_by_date_region)


# In[ ]:




