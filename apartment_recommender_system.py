# -*- coding: utf-8 -*-
"""Apartment recommender system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P8a_ZQ9ekV9lq3A5dU5AAMHV5Datua2W
"""

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd


df = pd.read_excel('/Users/amarahmed/Desktop/apt_loc_prj/content/sample_data/A.L.I.xlsx')
df1=df.iloc[:,:34]
df1 =df1.fillna(0)

df_new = df1.iloc[:,1:]

user_inputs = []
print('Enter 1 if you like, 0 if you do not like  ,skip if you are not interested')
for column_name in df_new.columns:
    while True:
        user_input = input("Enter 0 or 1 or skip, The apartment with " + column_name + ": ")
        if user_input == "skip":
            user_input = "0"
        if user_input in ['0', '1','skip']:
            break
        print("Invalid input! Please enter 0 or 1 or skip.")

    # Append the valid input to the list
    user_inputs.append(user_input)

user_inputs=  [int(i) for i in user_inputs]
user_interactions = np.array(user_inputs)

similarity_scores = cosine_similarity(user_interactions.reshape(1, -1), df_new)
recommended_items = np.argsort(similarity_scores)[0][::-1]  # reverse sort order


for item in recommended_items:
  similarity_percent = similarity_scores[0][item] * 100
  if(similarity_percent >= 70):
    print(f'{df1.iloc[item,0]},  ({similarity_percent:.2f}%)')

#from google.colab import drive
#drive.mount('/content/drive')