import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import json

np.random.seed(10)
x1 = np.linspace(0.1,5,100)
x2 = np.linspace(5.1,10,100)
y  = np.random.randint(0,100,100)

df1 = pd.DataFrame({'x':x1,'y':y})
df2 = pd.DataFrame({'x':x1,'y':y})
df3 = pd.DataFrame({'x':x2,'y':y})

df = pd.concat([df1,df2,df3])

data = [go.Scatter(x=df['x'], y = df['y'], mode = "markers")]
layout = go.Layout(title="Selction Graph", xaxis = {'title':'X' ,'color':'violet'}, yaxis={'title':'Y','color':'green'},hovermode='closest')
figure = {'data':data, 'layout':layout}
app = dash.Dash()

app.layout = html.Div([
                    html.H1("Selection",style={'textAlign':'center','color':'teal'}),
                    dcc.Graph(id="selection-graph",figure=figure),
                    html.Div([
                            # html.Pre(id = "density" ,style={'padding-top':25}),
                            html.H1(id = "density" ,style={'padding-top':25}),
                       ],style={'dsiplay':"inline-block","width":"30%",'verticalAlign':'top'})

])
@app.callback(Output('density','children'),
             [Input('selection-graph','selectedData')])
def find_density(selectedData):
    no_of_points = len(selectedData['points'])
    x_min = selectedData['range']['x'][0]
    x_max = selectedData['range']['x'][1]
    y_min = selectedData['range']['y'][0]
    y_max = selectedData['range']['y'][1]

    area = (y_max-y_min)*(x_max-x_min)

    density = no_of_points/area
    return "Density of the points in the seleted region is {:.2f}".format(density)
    # return json.dumps(selectedData,indent = 2)

if __name__ == "__main__":
    app.run_server()
