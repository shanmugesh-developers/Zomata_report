import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("/Users/Lenovo/Documents/intern/machine learning/Zomato.csv")
print(dataframe.head( ))

def handleRate(value):
      value=str(value).split('/')
      value=value[0];
      return float(value)

dataframe['rate']=dataframe['rate']
print(dataframe.head())

dataframe.info()

sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel('type of restaurant')

grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c="green",marker="o")
plt.xlabel("type of resarunt",c="red",size=20)
plt.ylabel("votes",c="red",size=20)

max_votes=dataframe['votes'].max( )
restaurant_with_max_votes=dataframe.loc[dataframe['votes'] == max_votes,'name']
print("restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)

plt.hist(dataframe['rate'], bins=5)
plt.title("ratings distribution")
plt.show( )

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

plt.figure(figsize=(6,6))
sns.boxplot (x='online_order', y='rate', data=dataframe)

pivot_table=dataframe.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
plt.title("heatmap")
plt.xlabel("online order")
plt.ylabel("listed in (type)")
plt.show()









