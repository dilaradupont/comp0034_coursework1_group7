from pathlib import Path
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
from Multi_Page.StartingBusiness import app
import base64



#Loading the picture

test_png = Path(__file__).parent.joinpath("Screenshot_1.png")
test_base64 = base64.b64encode(open(test_png, 'rb').read()).decode('ascii')

#Configuring the Layout

about_us = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br()])),
    dbc.Row(children=[
        html.H3("Inspiring Future Potentials", id="about_us", )]),
    dbc.Row(children=[
        html.P(
            "We are a team of four engineering students, who are completing a project on displaying data in a non-misleading "
            "way. Our aim was to create a range of charts, that would be able show which factors influence the ease of "
            "starting up a business.")]),
    dbc.Row(children=[
        dbc.Col(width=4),
        dbc.Col(html.Img(src='data:image/png;base64,{}'.format(test_base64), height=300, width=500),
                style={'left': '50%'}),
        dbc.Col(width=4)]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),
    dbc.Row(children=[
        html.P("While developing the charts the team has followed different software engineering techniques. The whole "
           "process of creating the 'Starting a business' app is well documented in a weekly minutes file. Throughout "
           "weekly meetings, both online and in person, the app has been built and modified to give the user the best experience possible. "
            "Further versions of the app will be released in the future following possible suggestions made by the users. Please do not hesitate to contact us for any information")]),
    dbc.Row(
        dbc.Col(children=[html.Br()])),
])

if __name__ == '__main__':
    app.run_server(debug=True)
