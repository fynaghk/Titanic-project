# import libraries
import numpy as np 
import pandas as pd 

# read dataset 
dataset = pd.read_csv('train.csv')

# numbers of rows and columns of dataset
print(dataset.shape)

# print first 10 rows from dataset
print(dataset.head(10))

# check duplicated data
print(dataset.duplicated().sum())

# detect missing values
print(dataset.isnull().sum())

# remove rows which have missing values
dataset.drop('Cabin', axis=1, inplace=True)
dataset.dropna(inplace=True)

# detect missing values again
print(dataset.isnull().sum())

# check datatypes
print(dataset.dtypes)