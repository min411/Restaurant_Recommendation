# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:05:15 2023

@author: kakoi
"""
import json
import pandas as pd

data_file = open("yelp_academic_dataset_review.json")
data = []
for line in data_file:
    data.append(json.loads(line))
review_df = pd.DataFrame(data)
data_file.close()

data_file_business = open("yelp_academic_dataset_business.json")
data_business = []
for line in data_file_business:
    data_business.append(json.loads(line))
business_df = pd.DataFrame(data_business)
data_file_business.close()

#merge two dfs so that the big df will have business name
#clean data so that only restaurants will be listed. 'Restaurants' in categories