#######
# Objective: Using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assign each day to its own trace.
######

# Perform imports here:
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go



# Create a pandas DataFrame from 2010YumaAZ.csv
tempdf = pd.read_csv('/home/drishtant/web_development_bootcamp_django/my_django_stuff/Plotly-Dashboards-with-Dash-master/Data/2010YumaAZ.csv')
tempdf2=tempdf.drop('LST_DATE',axis=1)
tempdf2.set_index('DAY')

tempdf2[tempdf2['DAY']=='TUESDAY']


# Use a for loop (or list comprehension to create traces for the data list)
data = [go.Scatter(x = tempdf2[tempdf2['DAY']==name]['LST_TIME'],y = tempdf2[tempdf2['DAY']==name]['T_HR_AVG'],
                   mode="lines+markers",name=name) for name in tempdf2['DAY'].unique()]


# Define the layout
layout = go.Layout(title="Temperature Data from june 1 2010 to june 7 2010",
                   xaxis={'title':'Time', 'color':'red'},
                   yaxis={'title':'Temperature','color':'red'})




# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)
