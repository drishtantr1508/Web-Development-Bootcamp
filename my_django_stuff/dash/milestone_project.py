import pandas as pd
import pandas_datareader as pdr
import dash
import  dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
import plotly.graph_objs as go
from dash.dependencies import Input, Output,State

def trim(df):
    x=[]
    for i in df:
        x.append(i[1])
    return x

app = dash.Dash()
companies = [
                {'label':'Amazon','value':'AMZN'},
                {'label':'Microsoft','value':'MSFT'},
                {'label':'Alphabet / Google','value':'GOOGL'},
                {'label':'Facebook','value':'FB'},
                {'label':'Alibaba','value':'BABA'},
                {'label':'Apple','value':'AAPL'},
                {'label':'Visa','value':'V'},
                {'label':'Taiwan Semiconductor','value':'TSM'},
                {'label':'Berkshire Hathaway','value':'BRK.A'},
                {'label':'Walmart','value':'WMT'},
                {'label':'Johnson & Johnson','value':'JNJ'},
                {'label':'Procter & Gamble','value':'PG'},
                {'label':'Mastercard','value':'MA'},
                {'label':'NVIDIA','value':'NVDA'},
                {'label':'Disney','value':'DIS'},
                {'label':'Adobe','value':'ADBE'},
                {'label':'Netflix','value':'NFLX'},
                {'label':'PayPal','value':'PYPL'},
                {'label':'Intel','value':'INTC'},
                {'label':'Cisco Systems','value':'CSCO'},
                #{'label':'Reliance Digital','value':'RIL'}
            ]
app.layout = html.Div([
                    html.H1("Stock Picker By Devil Drai",style={'color':'teal','textAlign':'center'}),
                    html.H3("Select Start Date",style={'display':'inline-block','marginLeft':25,}),
                    dcc.DatePickerSingle(
                    id='date-picker-start',
                    date=dt(2015, 5, 10),
                    style={'marginLeft':25,'display':'inline-block'}
                    ),
                    html.H3("Select End Date",style={'display':'inline-block','marginLeft':25,}),
                    dcc.DatePickerSingle(
                    id='date-picker-end',
                    date=dt(2020, 9, 4),
                    style={'marginLeft':25,'display':'inline-block'}
                    ),
                    html.Br(),
                    html.Br(),
                    dcc.Dropdown(id="companies",
                    options=companies,
                        multi=True,
                        ),
                    html.Div(id="check"),
                    html.Br(),
                    html.Button(id="update",children="Update",n_clicks=0),
                    html.Br(),
                    dcc.Graph(id="stock-graph")
])

@app.callback(Output('stock-graph','figure'),
             [Input('update','n_clicks')],
             [State('date-picker-start','date'),
              State('date-picker-end','date'),
              State('companies','value')])
def stock_graph(n_clicks,start,end,value):
    traces = []
    for company in value:
        df = pdr.get_data_tiingo(company, api_key=('2bb6f0056c2f72dc30f454cc1ed58ba5fd1dea29'),start=start,end=end)
        x_val = trim(df.index)
        traces.append(go.Scatter(x=x_val,y=(df.close),name=company))
    layout = go.Layout(title="Comparison of Stock value between listed Companies",
                        xaxis=dict(title="Stock Timeline",color="violet"),
                        yaxis=dict(title="Stock Value",color="green"))
    return {"data":traces,'layout':layout}

if __name__ == "__main__":
    app.run_server()
