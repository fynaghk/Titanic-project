# import libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# read dataset 
dataset = pd.read_csv('train.csv')

# remove rows which have missing values
dataset.drop('Ticket', axis=1, inplace=True)
dataset.drop('Cabin', axis=1, inplace=True)
dataset.dropna(inplace=True)

# check ages of people
print(dataset['Age'].describe())

# find median and IQR of Ages
print('Median:', dataset['Age'].median())
print('IQR:', dataset['Age'].quantile(q=0.75) - dataset['Age'].quantile(q=0.25))

# check survival is adult or child
dataset['categorize_age'] = pd.Series()
for i in dataset.index:
    if dataset.loc[i, 'Age'] <= 16:
        dataset.at[i, 'category'] = 'child'
    elif dataset.loc[i, 'Age'] <= 25:
        dataset.at[i, 'category'] = 'young'
    elif dataset.loc[i, 'Age'] <= 60:
        dataset.at[i, 'category'] = 'adult'
    else:
        dataset.at[i, 'category'] = 'old'

# numbers of survivals based on age category
print(dataset['category'].value_counts())

# data visualization \
#FIRST
cross_table_ages = pd.crosstab(dataset['Age'], dataset['category']).reindex(['child', 'young', 'adult', 'old'], axis=1)
print(cross_table_ages)
print(dataset.hist()) 