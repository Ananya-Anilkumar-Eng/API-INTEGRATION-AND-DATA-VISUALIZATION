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

fig=px.scatter_3d(df[:5],x='population',y='state',z='deaths')
fig.show()
