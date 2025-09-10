#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[9]:


df = pd.read_csv("adult.csv")
print(df.head())


# In[10]:


plt.figure(figsize=(12, 6))
sns.countplot(data=df, x="education", hue="marital-status")
plt.xlabel("Education Level")
plt.ylabel("Count")
plt.title("Marital Status by Education Level")
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[11]:


edu_counts = df["education"].value_counts()
marital_counts = df["marital-status"].value_counts()

print("Education Level Counts:\n", edu_counts)
print("\nMarital Status Counts:\n", marital_counts)


# In[12]:


if "hours-per-week" in df.columns:
    mean_hours_by_edu = df.groupby("education")["hours-per-week"].mean()
    print("\nAverage Hours per Week by Education:\n", mean_hours_by_edu)

    mean_hours_by_edu.plot(kind="bar", figsize=(10, 5), title="Average Hours Worked per Week by Education", color="skyblue")
    plt.ylabel("Average Hours/Week")
    plt.xlabel("Education")
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# In[13]:


if "hours-per-week" in df.columns:
    q1 = df["hours-per-week"].quantile(0.25)
    q2 = df["hours-per-week"].quantile(0.5)
    q3 = df["hours-per-week"].quantile(0.75)

    print("\nQuantiles for 'hours-per-week':")
    print("25th Percentile:", q1)
    print("50th Percentile (Median):", q2)
    print("75th Percentile:", q3)

    plt.boxplot(df["hours-per-week"])
    plt.title("Boxplot of Hours Worked per Week")
    plt.ylabel("Hours per Week")
    plt.grid()
    plt.show()


# In[ ]:




