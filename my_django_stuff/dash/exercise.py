import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input , Output , State

app = dash.Dash()

app.layout = html.Div([
                    dcc.RangeSlider(id="input_slider",
                    marks={i: 'Label {}'.format(i) for i in range(-11, 12,1)},
                    min=-11,
                    max=11,
                    value=[0, 0]
                    ),
                    html.Button(id="submit-button",children="Submit Here",n_clicks=0),
                    html.H1(id="Output-div")
])

@app.callback(Output("Output-div","children"),
             [Input("submit-button","n_clicks")],
             [State('input_slider','value')])
def update_output(n_clicks,input):
    return f'{input[0]*input[1]} is the output and button was clicked {n_clicks} time'

if __name__ == "__main__":
    app.run_server()
