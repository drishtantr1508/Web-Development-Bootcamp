import dash
import dash_core_components as dcc
import dash_html_components as html
import json
from dash.dependencies import Input , Output , State
import pandas as pd
import plotly.graph_objs as go
import base64

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app = dash.Dash()

df = pd.read_csv('Data/wheels.csv')

data = [go.Scatter(x=df['color'],y=df['wheels'],mode="markers",marker={'size':12,'opacity':0.6})]

layout = go.Layout(title="Testing Hovering Capabilities in Plotly",xaxis={'title':'COLOR','color':'violet'},
                    yaxis={'title':'WHEELS','color':'green'},hovermode='closest')

app.layout = html.Div([
                    html.H1("Hovering in Dash",style={'textAlign':"center",'color':"teal"},),
                    dcc.Graph(id="graph",figure={'data':data,'layout':layout},style={'width':'50%','float':'left'}),
                    html.Div(
                            # html.Div(html.Pre(id="json_input")),
                            html.Img(id="json_input",src="children",height=300),
                            style={'width':'30%','float':'right','margin-right':'15%'}
                            )

])
@app.callback(Output('json_input','src'),
             [Input('graph','hoverData')])#we can use clickData if we want to click effect instead of hovering ...
def hover_data(hoverData):
    wheels = hoverData['points'][0]['y']
    color = hoverData['points'][0]['x']
    path = "/home/drishtant/web_development_bootcamp_django/my_django_stuff/dash/Data/Images/"
    return encode_image(path+df[(df['wheels']==wheels) & (df['color']==color)]['image'].values[0])
    # return json.dumps(hoverData)
if __name__ == "__main__":
    app.run_server()
