#-------------------- Imports--------------------#

import plotly.express as px
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
from Multi_Page.StartingBusiness import app
import os
import pathlib as Path

#-----------------StyleSheet---------------------#

external_stylesheets = [dbc.themes.COSMO]

#----------------Data&Lists----------------------#

#df = pd.read_csv('apps/Choropleth_Map/DBresorted_cm.csv')
df_path = os.path.join("apps", "Choropleth_Map")
df = pd.read_csv(os.path.join(df_path, "DBresorted_cm.csv"))
indicator_choropleth_list = ['Starting a business - Score',
                             'Starting a business: Cost - Average (% of income per capita) - Score',
                             'Starting a business: Procedures required - Average (number) - Score',
                             'Starting a business: Time - Average (days) - Score',
                             'Starting a business: Paid-in Minimum capital (% of income per capita) - Score']

region_choropleth_list = ['World', 'South Asia', 'Middle East & North Africa', 'Europe & Central Asia',
                          'Sub-Saharan Africa', 'Latin America & Caribbean', 'East Asia & Pacific',
                          'North America']

income_choropleth_list = ['All', 'Low income', 'Upper middle income', 'Lower middle income', 'High income']

#------------------------ChoroplethMap-----------------------------#

front_page = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row([
        dbc.Col(width=4, children=[

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

            html.H5("Top 10 charts"),
            dcc.Graph(id='barchart'),

            html.H5("Select Bar Chart Year"),
            dcc.Dropdown(
                id='year',
                options=[{'value': x, 'label': x} for x in list(range(2006,2021,1))],
                value=2006,
                clearable=False,
                multi=False),
            html.Br()
        ]),

        dbc.Col(width=8, children=[
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

#----------------------------Layout----------------------------#

app.layout = front_page

#---------------------------Callbacks--------------------------#

@app.callback(
    [Output("choropleth", "figure"), Output("barchart", "figure")],
    [Input("indicator", "value")], [Input("region", "value")], [Input("income", "value")], [Input("year", "value")])  # Here the input is captured
def update_output(indicator, region, income, year):

    # When no values are selected from multi choice go to home graph of region and income group
    if len(region) == 0:
        region = ['World']
    if len(income) == 0:
        income = ['All']

    if 'World' not in region:
        df_choropleth = df.loc[df['Region'].isin(region)]
        fitbound_value_cm = 'locations'
    else:
        df_choropleth = df
        fitbound_value_cm = False

    if 'All' not in income:
        df_choropleth = df_choropleth.loc[df['Income Group'].isin(income)]
    else:
        df_choropleth = df_choropleth

    fig_cm = px.choropleth(df_choropleth, locations="Country Code",
                           color=indicator,
                           hover_name="Country Name",
                           projection='natural earth',
                           title=str(indicator),
                           animation_frame='Year',
                           hover_data={'Country Code': False},
                           color_continuous_scale=px.colors.sequential.Plasma,
                           fitbounds=fitbound_value_cm,
                           range_color=[0, 100])

    fig_cm.update_layout(title=dict(font=dict(size=20)),
                         margin=dict(l=15, r=15, t=35, b=5),
                         coloraxis_colorbar=dict(title="Score"))

    df_bc = df_choropleth.loc[df_choropleth['Year'] == year]
    df_bc.sort_values(by=[str(indicator)], inplace=True, ascending=False)
    df_bc = df_bc.head(10)
    df_bc = df_bc[df_bc[str(indicator)].notna()]
    df_bc.sort_values(by=[str(indicator)], inplace=True, ascending=True)

    if df_bc[str(indicator)].count() in range(3, 11):
        list_pos_color = ['Runners up' for i in range(1, df_bc[str(indicator)].count() - 2)]
        list_pos_color.extend(('Third', 'Second', 'First'))
    elif df_bc[str(indicator)].count() == 3:
        list_pos_color = ['Third', 'Second', 'First']
    elif df_bc[str(indicator)].count() == 2:
        list_pos_color = ['Second', 'First']
    elif df_bc[str(indicator)].count() == 1:
        list_pos_color = ['First']
    else:
        list_pos_color = []

    fig_bc = px.bar(df_bc, x=indicator, y='Country Name', orientation='h', labels={str(indicator): 'Score'},
                    hover_data={'Country Name': False}, color=list_pos_color, text='Country Name',
                    color_discrete_map={'First': 'rgb(255,215,0)',
                                        'Second': 'rgb(192,192,192)',
                                        'Third': 'rgb(205, 127, 50)',
                                        'Runners up': 'rgb(204, 229, 255)'})

    fig_bc.update_yaxes(visible=False, showticklabels=False)

    return fig_cm, fig_bc

#-----------------------Isolated Excecution Option------------------------------#

if __name__ == '__main__':
    app.run_server(debug=True)