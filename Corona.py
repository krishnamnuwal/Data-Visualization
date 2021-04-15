##importing all the required modules
import csv
import pandas as  pd 
import plotly.express as px
import plotly

##storing the data in df variable in the form of dataframe
df=pd.read_csv('data.csv')
##print(df)

##creating a scatter graph between cases and date on their respective axis
fig=px.scatter(df,x="date",y="cases",color="country")

##creating the 3d scatter graph between date,cases,countries on their respective axis
#fig=px.scatter_3d(df,x="date",y="cases",z="country",color="country", opacity=0.7)
plotly.offline.plot(fig)



