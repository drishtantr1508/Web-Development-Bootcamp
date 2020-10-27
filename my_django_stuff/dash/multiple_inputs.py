import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np

df = pd.read_csv("/home/drishtant/web_development_bootcamp_django/my_django_stuff/dash/Data/mpg.csv")

xaxis_options = [{'label':str(obj),'value':obj}  for obj in df.columns[:-1]]
yaxis_options = [{'label':str(obj),'value':obj}  for obj in df.columns[:-1]]

app = dash.Dash()
app.layout = html.Div([
                 html.H1("Multiple Inputs",style={'textAlign':'center','color':'teal'}),
                 html.Br(),
                 html.Div([
                        html.Span("X-axis",style={'textAlign':'left'}),
                        html.Span("Y-axis",style={'float':'right'}),
                        ]),
                 html.Br(),
                 html.Div([
                        dcc.Dropdown(id='x-axis',options=xaxis_options,value='mpg',style={'width':'50%','float':'left'}),
                        dcc.Dropdown(id='y-axis',options=yaxis_options,value='weight',style={'width':'50%','float':'right'})
                 ]),
                 html.Br(),
                 html.Br(),
                 html.Br(),
                 dcc.Graph(id="mpg-graph"),
])





@app.callback(Output('mpg-graph','figure'),
             [Input('x-axis','value'),
              Input('y-axis','value')])
def update_graph(x_param,y_param):
    data = [go.Scatter(x=df[x_param],y=df[y_param],mode="markers",marker={'size':9,'opacity':0.5,'color':'teal','line':{'width':0.5,'color':'black'}})]
    layout = go.Layout(title="{} vs {}".format(x_param.upper(),y_param.upper()),
                       xaxis={'title': x_param.upper(), 'color':'violet'},
                       yaxis={'title': y_param.upper(), 'color':'blue'},hovermode='closest')
    return {'data':data,'layout':layout}

if __name__ == "__main__":
    app.run_server()
