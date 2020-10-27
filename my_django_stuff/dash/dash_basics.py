import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

app = dash.Dash()
colors={'background':"black",'text':'teal'}
x_values = np.linspace(1,101,1000)
y_values = np.random.randn(1000)
trace0 = go.Scatter(x=x_values,y=y_values+5, mode="markers",marker=dict(size=6,color='green'))
trace1 = go.Scatter(x=x_values,y=y_values, mode="lines",marker=dict(size=3,color='orange'))
trace2 = go.Scatter(x=x_values,y=y_values-5, mode="lines+markers",marker=dict(size=3,color='teal'))
data1=[trace0,trace1,trace2]
layout1 = go.Layout(title='Hello Second  Plot',xaxis={'title':"My X Axis"}, yaxis=dict(title="My Y Axis"),hovermode='closest', font={'color':colors['text']})

random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data2 = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(size=12,
                                color='teal',
                                symbol = 'pentagon', line=dict(width=2))

                        )]
layout2 = go.Layout(title='Hello First Plot',xaxis={'title':"My X Axis"}, yaxis=dict(title="My Y Axis"),hovermode='closest',plot_bgcolor=colors['background'])

np.random.seed(42)
colors={'background':"grey",'text':'teal'}
app.layout = html.Div(children=[
               html.H1("Hello Dash",style={'textAlign':'center','color':colors['text']}),
               html.Div("Dash Application with python"),
               html.H1("SCATTER PLOT"),
               html.Div(["this is div 2"],id="div2",style={'color':'red','border':'2px solid blue','background-color':'teal','max-width':'50%'}),
               html.Br(),
               dcc.Graph(id='example1',
                        figure={'data':data2,'layout':layout2}),
               html.H1("LINE PLOT"),
               dcc.Graph(id='example2',
                        figure={'data':data1,'layout':layout1})
])

if __name__ == '__main__':
    app.run_server()
