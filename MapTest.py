
import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd


external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Data and lists
df = pd.read_csv('Data Set/DBresorted_cm.csv')

indicator_choropleth_list = ['Starting a business - Score',
                             'Starting a business: Cost - Average (% of income per capita) - Score',
                             'Starting a business: Procedures required - Average (number) - Score',
                             'Starting a business: Time - Average (days) - Score',
                             'Starting a business: Paid-in Minimum capital (% of income per capita) - Score']

region_choropleth_list = ['World', 'South Asia', 'Middle East & North Africa', 'Europe & Central Asia',
                          'Sub-Saharan Africa', 'Latin America & Caribbean', 'East Asia & Pacific',
                          'North America']

income_choropleth_list = ['All', 'Low income', 'Upper middle income', 'Lower middle income', 'High income']
#---------------------------------------------------------------
"""
app.layout = html.Div([
    html.Div([
        html.P("Indicator:"), # to be removed/changed appropriately
        dcc.Dropdown(
            id='indicator',
            options=[{'value': x, 'label': x}
                     for x in indicator_choropleth_list],
            value=indicator_choropleth_list[0]
        ),
        dcc.Dropdown(
            id='region',
            options=[{'value': x, 'label': x}
                     for x in region_choropleth_list],
            value=region_choropleth_list[0]
        ),
        dcc.Dropdown(
            id='income',
            options=[{'value': x, 'label': x}
                     for x in income_choropleth_list],
            value=income_choropleth_list[0]
        ),
        dcc.Graph(id='choropleth')
    ]),
])
"""

front_page = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row([
        dbc.Col(width=3, children=[

            html.H5("Select Region"),
            dcc.Dropdown(
                id='region',
                options=[{'value': x, 'label': x} for x in region_choropleth_list],
                value=region_choropleth_list[0],
                clearable=False,
                multi=True),
            html.Br(),

            html.H5("Select Income Group"),
            dcc.Dropdown(
                id='income',
                options=[{'value': x, 'label': x} for x in income_choropleth_list],
                value=income_choropleth_list[0],
                clearable=False,
                multi=True),
            html.Br(),
        ]),

        dbc.Col(width=9, children=[
            html.H5("Select Indicator"),
            dcc.Dropdown(
                id='indicator',
                options=[{'value': x, 'label': x} for x in indicator_choropleth_list],
                value=indicator_choropleth_list[0],
                clearable=False),
            html.Br(),
            dcc.Graph(id='choropleth'),
        ]),
    ]),
])

app.layout = front_page
#---------------------------------------------------------------


@app.callback(
    Output("choropleth", "figure"),
    [Input("indicator", "value")], [Input("region", "value")], [Input("income", "value")])  # Here the input is captured
def update_output(indicator, region, income):

    # When no values are selected from multi choice go to home graph of region and income group
    if len(region) == 0:
        region = ['World']
    if len(income) == 0:
        income = ['All']

    if 'World' not in region:
        df_choropleth = df.loc[df['Region'].isin(region)]
        fitbound_value = 'locations'
    else:
        df_choropleth = df
        fitbound_value = False

    if 'All' not in income:
        df_choropleth = df_choropleth.loc[df['Income Group'].isin(income)]
    else:
        df_choropleth = df_choropleth

    fig = px.choropleth(df_choropleth, locations="Country Code",
                        color=indicator,
                        hover_name="Country Name",
                        projection='natural earth',
                        title=str(indicator),
                        animation_frame='Year',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        fitbounds=fitbound_value,
                        range_color=[0, 100])

    fig.update_layout(title=dict(font=dict(size=20)),
                      margin=dict(l=15, r=15, t=35, b=5))

    fig.update_layout(coloraxis_colorbar=dict(title="Score"))

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)