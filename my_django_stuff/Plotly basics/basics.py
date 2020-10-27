import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

###########

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data1 = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(size=12,
                                color='teal',
                                symbol = 'pentagon', line=dict(width=2))

                        )]
layout = go.Layout(title='Hello First Plot',xaxis={'title':"My X Axis"}, yaxis=dict(title="My Y Axis"),hovermode='closest')
# fig1 = go.Figure(data=data1,layout=layout)
# pyo.plot(fig1,filename ='scatter.html')

###########

x_values = np.linspace(1,101,1000)
y_values = np.random.randn(1000)
trace0 = go.Scatter(x=x_values,y=y_values+5, mode="markers",marker=dict(size=6,color='green'))
trace1 = go.Scatter(x=x_values,y=y_values, mode="lines",marker=dict(size=3,color='orange'))
trace2 = go.Scatter(x=x_values,y=y_values-5, mode="lines+markers",marker=dict(size=3,color='teal'))
data2=[trace0,trace1,trace2]
layout = go.Layout(title='Hello Second  Plot',xaxis={'title':"My X Axis"}, yaxis=dict(title="My Y Axis"),hovermode='closest')
fig2 = go.Figure(data=data2,layout=layout)
pyo.plot(fig2,filename ='scatter.html')
