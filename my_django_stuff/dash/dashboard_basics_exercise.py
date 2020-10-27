import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as  np
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('Data/OldFaithful.csv')

x_values = df['X']
y_values = df['Y']
trace0 = go.Scatter(x= x_values, y=y_values,mode="markers", marker=dict(size=9,color="red"))
data = [trace0]
layout = go.Layout(title = "Eruption Duration vs Eruption Interval", xaxis = {'title':"Eruption Duration"}, yaxis ={'title':"Eruption Interval"})

app.layout = html.Div(children=[
                html.H1  ("Old Faithful",style={'textAlign':'center','color':"teal"}),
                html.H5  ("Old Faithful is a cone geyser located in YellowStone National Park in Wyoming , United States"),
                html.H5  ("Since 2000 its intervals have varied from 44 to 125 minutes between eruptions. And it has been Found that It shows it has been following a bipolar model as can be seen from the data plotted below."),
                dcc.Graph(id='example',
                          figure={'data':data,'layout':layout})
])

if __name__ == "__main__":
    app.run_server()
