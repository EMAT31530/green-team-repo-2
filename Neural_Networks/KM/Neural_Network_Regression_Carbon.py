#! /usr/bin/env python
# coding: utf-8

# import modules
import pandas as pd
import numpy as np
import sklearn as skl

# pull dataset
data = pd.read_pickle("./nutrition_data_clean.pkl")

# drop food group and brand columns
print(list(data.columns))
data.drop(data.columns[1:3], axis=1, inplace=True)
print(list(data.columns))
data.drop(['Price (£)', 'Price per Weight (£/10Gram)'])
print(list(data.columns))