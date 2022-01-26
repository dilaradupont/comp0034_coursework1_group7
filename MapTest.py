
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

#---------------------------------------------------------------


@app.callback(
    Output("choropleth", "figure"),
    [Input("indicator", "value")], [Input("region", "value")], [Input("income", "value")])  # Here the input is captured
def update_output(indicator, region, income):

    if region != 'World':
        df_sub = df.loc[df['Region'] == region]
    else:
        df_sub = df

    if income != 'All':
        df_sub = df_sub.loc[df['Income Group'] == income]
    else:
        df_sub = df_sub

    fig = px.choropleth(df_sub, locations="Country Code",
                        color=indicator,
                        hover_name="Country Name",
                        projection='natural earth',
                        title=str(indicator),
                        animation_frame='Year',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        fitbounds='locations')

    fig.update_layout(title=dict(font=dict(size=28), x=0.5, xanchor='center'),
                      margin=dict(l=250, r=10, t=50, b=50))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)