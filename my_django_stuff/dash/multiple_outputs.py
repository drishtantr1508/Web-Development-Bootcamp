import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.graph_objs as go
import base64

app = dash.Dash()

df = pd.read_csv('/home/drishtant/web_development_bootcamp_django/my_django_stuff/dash/Data/wheels.csv')

def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())


app.layout = html.Div([
                    html.H1("Multiple Outputs",style={'textAlign':'center','color':'teal'}),
                    html.Div([
                        dcc.RadioItems(id="wheels",options=[{'label':i,'value':i}
                            for i in df['wheels'].unique()],value=df['wheels'].unique()[0]),
                        html.Div(id="wheels-output")
                    ]),
                    html.Hr(),
                    html.Div([
                        dcc.RadioItems(id="color",options=[{'label':i,'value':i}
                            for i in df['color'].unique()],value=df['color'].unique()[0]),
                        html.Div(id="color-output")
                    ]),
                    html.Hr(),
                    html.Img(id='image-output', src='children', height=300)

                ])

@app.callback(Output("wheels-output","children"),
             [Input("wheels","value")])
def wheel_update(wheels_value):
    return "You have Chosen {}".format(wheels_value)

@app.callback(Output("color-output","children"),
             [Input("color","value")])
def color_update(color_value):
    return "You have Chosen {}".format(color_value)

@app.callback(
    Output('image-output', 'src'),
    [Input('wheels', 'value'),
     Input('color', 'value')])
def callback_image(wheel, color):
    path = '/home/drishtant/web_development_bootcamp_django/my_django_stuff/dash/Data/Images/'
    return encode_image(path+df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0])


if __name__ == "__main__":
    app.run_server()
