#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

#
df = pd.read_csv('lab4.csv')


population_mean_pd = df['Population'].mean()
gdp_std_pd = df['GDP'].std()
population_max_np = np.max(df['Population'])
gdp_min_np = np.min(df['GDP'])
population_sum_np = np.sum(df['Population'])

print(population_mean_pd)
print(gdp_std_pd)
print(population_max_np)
print(gdp_min_np)
print(population_sum_np)

df['GDP'] = df['GDP'] * 1.10

df_indexed = df.set_index(['Country', 'Year'])
df_swapped = df_indexed.swaplevel().sort_index()

print(df_swapped.head())


df_unstacked = df_indexed.unstack(level='Year')

print(df_unstacked)

df_hierarchical = df.set_index(['Country', 'Year'])

china_population_trends = df_hierarchical.loc['China', 'Population']

print(china_population_trends)


# In[ ]:




