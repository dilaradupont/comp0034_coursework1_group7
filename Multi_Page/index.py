import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output
import pandas as pd
import plotly.express as px
from Multi_Page.apps.Bubble_Chart import Bubble_Chart_app
from Multi_Page.apps.Choropleth_Map import Choropleth_app
from Multi_Page.apps.Contact import Contact_app
from Multi_Page.apps.Radar_chart import Radar_Chart_app

from Multi_Page.StartingBusiness import app

app.title = "Business"

#---------------------------------------------------------------
#Creating the Navigation Bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("About us", href="/about-us")),
        dbc.NavItem(dbc.NavLink("Choropleth Map", href="/choropleth-map")),

        dbc.NavItem(dbc.NavLink("Bubble Chart", href="bubble-chart")),
        dbc.NavItem(dbc.NavLink("Radar Chart", href="radar-chart")),
    ],
    brand="Starting a Business",
    brand_href="http://127.0.0.1:8050/",
    color="primary",
    dark=True,
    links_left=True,
    fluid=True,
    sticky="top",


)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])

#index_layout = Choropleth_app.cm_bc_page


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))

def display_page(pathname):
    if pathname == '/choropleth-map':
        return Choropleth_app.cm_bc_page
    elif pathname == '/bubble-chart':
        return Bubble_Chart_app.bubblechart_page
    elif pathname == '/':
        return Choropleth_app.cm_bc_page
    elif pathname == '/radar-chart':
        return Radar_Chart_app.radar_page
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True)