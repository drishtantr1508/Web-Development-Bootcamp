import pandas as pd
import dash
import  dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State

app = dash.Dash()
degree = 3
app.layout = html.Div([
                html.H1("Playing with graphs in two dimension", style = {'color':'teal','textAlign':'center'}),
                html.H4("Enter the degree of the polynomial: "),
                dcc.Input(id="degree-input"),
                html.P(id="degree-output"),
                html.Div([dcc.Slider(id=str(slider),
                                min=-9999999999,
                                max=9999999999,
                                step=0.000000005,
                                value=0
                            ) for slider in range(degree)]),
                dcc.Graph(id="graph")
])
@app.callback(Output("graph","figure"),
             [Input(str(i),"value") for i in range(degree)])
def no_of_sliders(a,b,c):
    x = list(range(-9999,9999,1))
    y = [(a*x**2 + b*x +c) for x in x]
    data = [go.Scatter(x = x, y = y, mode="lines")]
    layout = go.Layout(title = "Quadratic")
    return {'data':data, 'layout':layout}


if __name__ == "__main__":
    app.run_server()
