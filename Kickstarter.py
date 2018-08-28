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

#print head 
print (ks.head())
print (ks.info())

#Scatter plot for usd_pledged and goal 
sns.lmplot(x='usd_pledged_real', y='usd_goal_real', data=ks)
plt.title('Goal vs Pledged')
plt.show()
 
#Scatter plot for backers and usd pledged 
sns.lmplot(x='backers', y='usd_pledged_real', data=ks)
plt.title('Backers vs Pledged')
plt.show()

#Histogram of backers 

ks['backers'].plot(kind='hist', rot=70, logx=False, logy=True)
plt.title('Distribution of Backers')
plt.xlabel('backers')
plt.show()

#Histogram of Total Pledged

ks['usd_pledged_real'].plot(kind='hist', rot=70, logx=False, logy=True)
plt.title('USD Pledged Real Distribution')
plt.xlabel('usd_pledged_real')

plt.show()

#Value counts of main category 

plt.figure(figsize=(8,8))
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

#Distribution of state, df=success rate %

df = round(ks["state"].value_counts()/len(ks["state"])*100,2)
print("State Success")
print(df)

#pie plot -- add stylings
plot = df.plot.pie(y='df', figsize=(5,5))
plt.show()

#Histogram of goals 
x = np.log(ks.goal + 1).head(100000)
x.plot.hist(bins=8)
plt.title('Goal Distribution')
plt.show()

y = np.log(ks.usd_pledged_real + 1).head(100000)
y.plot.hist(bins=8)
plt.title('USD Pledged Distribution')
plt.show()

#Distribution of state, df=success rate %

df = round(ks["state"].value_counts()/len(ks["state"])*100,2)
print("State Success")
print(df)

#Seperate DF'S into fail and successs
df_failed = ks[ks["state"] == "failed"]
df_success = ks[ks["state"] == "successful"]

#Create histogram data
x1 = np.log(df_failed['usd_goal_real']+1).head(100000)
x2 = np.log(df_success['usd_goal_real']+1).head(100000)

#Plot Failed and Success Histograms 
x1.plot.hist(bins=8)
x2.plot.hist(bins=8)
plt.title('Successful Projects vs Failed')
plt.show()

#Create categories for success and failure
main_cat = ks["main_category"].value_counts()
main_cat_failed = ks[ks["state"] == "failed"]["main_category"].value_counts()
main_cat_success = ks[ks["state"] == "successful"]["main_category"].value_counts()

#Create histograms for Categories & Successful/Failure

t1 = go.Bar (
	x=main_cat_failed.index,
	y=main_cat_failed.values,
	name="Failed Categories"
	)

t2 = go.Bar (
	x=main_cat_success.index,
	y=main_cat_success.values,
	name="Successful Categories"
	)

t3 = go.Bar(
	x=main_cat.index,
	y=main_cat.values,
	name='Distribution Across Categories'
	)

fig = tls.make_subplots(rows=2, cols=2, specs=[[{}, {}], [{'colspan': 2}, None]],
	
subplot_titles = ("Failed", "Successful", "General Categories"))

#setting the figs
fig.append_trace(t1, 1, 1)
fig.append_trace(t2, 1, 2)
fig.append_trace(t3, 2, 1)

#plot in browser
fig['layout'].update(showlegend=True, title="Main Category's Distribuition",bargap=0.05)
plot_url = py.plot(fig)



