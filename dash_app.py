# Copied from the Dash tutorial documentation at https://dash.plotly.com/layout on 24/05/2021
# Import section modified 10/10/2021 to comply with changes in the Dash library.

# Run this app with `python dash_app.py` and visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html

external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Business"

#navigation bar

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About us", href="http://127.0.0.1:8050/")),
        dbc.NavItem(dbc.NavLink("Contact", href="http://127.0.0.1:8050/")),

        dbc.NavItem(dbc.NavLink("Top 10", href="http://127.0.0.1:8050/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("By Income", href="#"),
                dbc.DropdownMenuItem("By Gender", href="#"),
                dbc.DropdownMenuItem("By Area", href="#"),
                dbc.DropdownMenuItem("By Growth", href="#"),
            ],
            nav= True,
            in_navbar=True,
            label ="Top 10",


        ),
    ],
    brand = "Starting a Business",
    brand_href="http://127.0.0.1:8050/",
    color = "primary",
    dark = True,
    links_left= True,
    fluid = True,
    sticky= "top",


)
#text
text = dbc.Container([
    dbc.Row(
        dbc.Col(html.H2("Starting a Business Dashboard (to be removed?)"), width='auto', xxl=5),
        justify="center"),
    #dbc.Row(html.H6("Helping you shape your future business.")


])

# assume you have a "long-form" data frame see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app.layout = html.Div(children=[
    #html.H1(children='Hello Dash'),

    #html.Div(children='''
        #Dash: A web application framework for Python.
    #'''),
    navbar,
    text,


    dcc.Graph(
        id='example-graph',
        figure=fig
=======
title = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Starting a Business Dashboard"), width='auto', xxl=3), justify='center'
    )
])

"""
app.layout = html.Div([
    html.H1(children='Starting a Business Dashboard'),
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ]),
    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])
])
"""

app.title = 'Doing Business'
app.layout = html.Div([title])

if __name__ == '__main__':
    app.run_server(debug=True)
