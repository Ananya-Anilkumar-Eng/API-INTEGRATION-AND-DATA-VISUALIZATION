import requests
import pandas as pd
import warnings as wg
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

wg.simplefilter(action="ignore",category=FutureWarning)
#Giving a request to access the required public api
url = "https://disease.sh/v3/covid-19/states"
response = requests.get(url)

#Converting to json format
data = response.json()

#Converting to datframe using pandas
df=pd.DataFrame(data)

#Histogram-Bar graph
sns.barplot(data=df[:20],x='deaths',y='state',color='red')
plt.title('Distribution of COVID-19 Deaths Across first 20 States')
plt.xlabel('Number of Deaths')
plt.ylabel('States')
plt.show()
sns.histplot(data=df[:15], x='population',color='blue')
plt.title('Distribution of Population Across first 15 States')
plt.xlabel('Population')
plt.ylabel('Count')
plt.show()

#Normal curves
sns.set(font_scale=1.5)
sns.catplot(x='population',y='state',data=df[:10],kind='point',capsize=0.4,errorbar=None,aspect=2,color='red')
plt.title('Distribution of Population Across first 10 States')
plt.xlabel('Population')
plt.ylabel('States')
plt.show()
sns.set(font_scale=1)
sns.relplot(x='population',y='state',data=df[:10],kind='line',errorbar=None,aspect=2,markers=True,dashes=False,color='red')
plt.title('Distribution of Population Across first 10 States')
plt.xlabel('Population')
plt.ylabel('States')
plt.show()

#Scatterplots, Density and Contour Plots
sns.set_style('white')
sns.kdeplot(data=df[:10],x='population',y='deaths')
plt.title('Distribution of COVID-19 death cases Across first 10 States')
plt.xlabel('Population')
plt.ylabel('Deaths')
plt.show()
sns.set_style('white')
sns.scatterplot(data=df[:10],x='population',y='deaths')
plt.title('Distribution of COVID-19 death cases Across first 10 States')
plt.xlabel('Population')
plt.ylabel('Deaths')
plt.show()

#3D Plot
fig=px.scatter_3d(df[:5],x='population',y='state',z='deaths')
fig.show()
