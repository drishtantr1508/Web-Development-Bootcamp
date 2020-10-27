import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo
import numpy as np

df = pd.read_csv("/home/drishtant/web_development_bootcamp_django/my_django_stuff/dash/Data/gapminderDataFiveYear.csv")
# figure = update_graph(selected_year)
app = dash.Dash()
app.layout = html.Div([
                        # dcc.Input(id = "my-id",value = "initial text",type="text"),
                        # html.Div(id = "my-div",style={'border':'2px solid blue'}),
                        # html.Br(),
                        # html.H1("Enter the first no: "),
                        # dcc.Input(id="value1",value="0",type="text"),
                        # html.Br(),
                        # html.H1("Enter the second no: "),
                        # dcc.Input(id="value2",value="0",type="text"),
                        # html.Br(),
                        # html.Div(id="sum",style={'border':'2px solid black'}),
                        # html.Br(),
                        dcc.Dropdown(id="year-picker",
                                    options=[
                                            {'label': '1952', 'value': 1952},
                                            {'label': '1957', 'value': 1957},
                                            {'label': '1962', 'value': 1962},
                                            {'label': '1967', 'value': 1967},
                                            {'label': '1972', 'value': 1972},
                                            {'label': '1977', 'value': 1977},
                                            {'label': '1982', 'value': 1982},
                                            {'label': '1987', 'value': 1987},
                                            {'label': '1992', 'value': 1992},
                                            {'label': '1997', 'value': 1997},
                                            {'label': '2002', 'value': 2002},
                                            {'label': '2007', 'value': 2007}
                                            ],
                                     value=1952),
                        dcc.Graph(id="graph"),



        ])

# @app.callback(Output(component_id="my-div",component_property="children"),
#              [Input(component_id="my-id",component_property="value")])
# def update_output(input_value):
#     return " You Entered {}".format(input_value)
#
# @app.callback([Input(component_id="value1",component_property="value")])
# def value1(input_value):
#     return input_value
#
# @app.callback([Input(component_id="value2",component_property="value")])
# def value2(input_value):
#     return input_value
#
# @app.callback([Output(component_id="sum",component_property="children")])
# def sum():
#     return value1()+ value2()

@app.callback(Output("graph","figure"),
             [Input("year-picker","value")])
def update_graph(selected_year):
    continents = list(df['continent'].unique())
    # print(continents)
    data = [go.Scatter(x=df[(df['continent']==continent) & (df['year']==selected_year)]['gdpPercap'],
                y=df[(df['continent']==continent) & (df['year']==selected_year)]['lifeExp'],
                mode="markers",opacity=0.6,name=continent,marker={'size':12},
                text=df[(df['continent']==continent) & (df['year']==selected_year)]['country']) for continent in continents]
    layout = go.Layout(title="GDP per Capita Income vs Life Expectancy Continentwise.",
                       xaxis={'title':'GDP Per Capita Income','type':'log'},
                       yaxis={'title':'Life Expectancy in {}'.format(selected_year)})

    return {'data':data, 'layout':layout}

if __name__ == "__main__":
    app.run_server()
