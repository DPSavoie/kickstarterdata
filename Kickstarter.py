#Dependencies 
import pandas as pd 
import numpy as np 

import matplotlib.pyplot as plt 
from matplotlib import cm 
import seaborn as sns  
color = sns.color_palette

import plotly.offline as py 
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.offline as offline
offline.init_notebook_mode()
import plotly.tools as tls

#read file 
ks = pd.read_csv("D:/Kickstarter/ks-projects-201801.csv")

#Time Series 

byDeadline = ks.groupby('deadline').mean()
plt.figure(figsize=(12,8))
byDeadline['usd_pledged_real'].plot
plt.title('Pledged time series')
plt.show()

#Scatter plot for usd_pledged and goal 
sns.lmplot(x='usd_goal_real', y='usd_pledged_real', data=ks)
plt.show()
 
#Scatter plot for backers and usd pledged 
sns.lmplot(X='backers', y='usd_pledged_real', data=ks)
plt.show()

#print head 
print (ks.head())
print (ks.info())

#Histogram of backers 

ks['backers'].plot(kind='hist', rot=70, logx=False, logy=True)
plt.xlabel('backers')

plt.show()

#Histogram of Total Sales

ks['usd_pledged_real'].plot(kind='hist', rot=70, logx=False, logy=True)
plt.xlabel('usd_pledged_real')

plt.show()

#Value counts of main category 

plt.figure(figsize=(15,8))
sector_name = ks['main_category'].value_counts()

sns.barplot(sector_name.values, sector_name.index)
for i, v in enumerate(sector_name.values):
    plt.text(0.8,i,v,color='k', fontsize=19)
    plt.xticks(rotation='vertical')
    plt.xlabel('count')
    plt.ylabel('Main Category')
    plt.title("Most Popular Categories")
    plt.grid(True)

plt.show()

