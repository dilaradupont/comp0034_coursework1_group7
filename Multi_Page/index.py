"""
This file is used to combine the different apps and help navigating between them through a navigation bar. It also
contains a footer element used across all pages.
"""
import dash_bootstrap_components as dbc
from dash import Input, Output
from dash import html, dcc
from Multi_Page.StartingBusiness import app
from Multi_Page.apps.About_Us import About_us_app
from Multi_Page.apps.Bubble_Chart import Bubble_Chart_app
from Multi_Page.apps.Choropleth_Map import Choropleth_app
from Multi_Page.apps.Radar_chart import Radar_Chart_app

app.title = "Business"

# -----------------------------------------Creating the Navigation Bar-------------------------------------------------#

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

# setting up the footer

footer = html.Footer("N. Zavaropoulos , D.D. Dupont, C. Vanelli Coralli, A. Ripa - IFP")

# setting up the the front page text

Welcome_text = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row(children=[
        html.H3("Starting a Business App", id="Intro", )]),

    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row(children=[
        html.P("The aim of our app is to encourage entrepreneurs "
               "from all around the world to start up their business. We do that by making data more accessible "
               "about the ease of setting up a business in a variety of countries and regions, based on different "
               "indicators: the number of procedures required, the cost, the entrepreneur's gender and the time required "
               "to set up a business. This available data is displayed in a variety of charts, and is aimed not only at "
               "entrepreneurs, but also anyone interested in finding out more about the factors that might influence the start "
               "up of a business. ", id="Intro_text")]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row(children=[
        html.H3("Functionality of the App", id="Questions", )]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),
    dbc.Row(children=[
        html.P("Are you an entrepreneur? A local administrator? Or simply a student? Our range of charts will help you "
               "figure out the impact certain regions or countries have on the ease of starting up a business.")]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),
    dbc.Row(children=[
        html.P("Our choropleth map not only enables you to choose which scores to display "
               "(time, cost, number of procedures, overall), but also to see the evolution of those scores in time by clicking on the play "
               "button on the year slider. Moreover, you can focus on specific geographical regions or income groups listed in a dropdown "
               "menu, and identify which are the best countries to start up a business by looking at the bar chart on the side.")]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),
    dbc.Row(children=[
        html.P(
            "If you want to analyse the relationship between the scores in time, cost and number of procedures required, the bubble chart "
            "displays how the indicators influence each other. You can tick boxes to select which regions and gender you want to look at. Below the "
            "bubble chart, you can find a table that is updated with the bubble chart, displaying the actual data for each indicator, rather than the "
            "given scores. ")]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),
    dbc.Row(children=[
        html.P(
            "If you are looking for a more detailed display of the gender inequalities in setting up a business, "
            "our radar chart will enable you to compare the number of procedures and time required to set up a business, "
            "as well as its cost, according to the entrepreneurs' gender. Clicking on 'Men' or 'Women' in the legend, will "
            "filter out the opposite option, enabling to focus on a single gender.")]),

], id="welcome-page")

# setting up the layout

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
    footer
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/choropleth-map':
        return Choropleth_app.cm_bc_page
    elif pathname == '/bubble-chart':
        return Bubble_Chart_app.bubblechart_page
    elif pathname == '/':
        return Welcome_text
    elif pathname == '/radar-chart':
        return Radar_Chart_app.radar_page
    elif pathname == '/about-us':
        return About_us_app.about_us
    else:
        return '404 Page Not Found'


if __name__ == '__main__':
    app.run_server(debug=True)
