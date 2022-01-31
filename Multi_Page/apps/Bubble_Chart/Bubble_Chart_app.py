# Copied from the Dash documetation sample code at https://github.com/plotly/dash-recipes/tree/master/multi-page-app
from dash import Input, Output, html, dcc
import dash_bootstrap_components as dbc
from Multi_Page.StartingBusiness import app

layout = dbc.Container(fluid=True, children=[
    html.Br(),
    html.H1('Fruit Selector'),
    dcc.Dropdown(
        id='app-2-dropdown',
        options=[
            {'label': '{}'.format(i), 'value': i} for i in [
                'Apple', 'Banana', 'Codsadsadconut', 'Date'
            ]
        ]
    ),
    html.Div(id='app-3-display-value')
])


@app.callback(Output('app-3-display-value', 'children'), Input('app-3-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
