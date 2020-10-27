import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(['Hello Dash',
                dcc.Dropdown(
                options=[
                    {'label': 'New York City', 'value': 'NYC'},
                    {'label': 'Montréal', 'value': 'MTL'},
                    {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='MTL'),
                html.Br(),
                dcc.Slider(
                    min=-5,
                    max=10,
                    step=0.0005,
                    value=-3
                ),
                html.Br(),
                dcc.Input(
                    placeholder='Enter a value...',
                    type='text',
                    value=''
                ),
                html.Br(),
                dcc.RadioItems(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': 'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'}
                    ],
                    value='MTL'
)
])
if __name__ == "__main__":
    app.run_server()
