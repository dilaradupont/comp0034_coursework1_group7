import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go

import plotly.io as pio

pio.renderers.default = "browser"

df_radar = pd.read_csv('./radar/radar_data.csv')

external_stylesheets = [dbc.themes.COSMO]
country_list = df_radar['Country Name'].unique()
year_list = list(range(2006, 2021))

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

radar_page = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row([
        dbc.Col(width=2, children=[
            html.Br(),
            html.H5('Select Country'),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in country_list],
                value=[],
                id="country",
                multi=True, 
            ),
            html.Br(),
            html.H5('Select Year'),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in year_list],
                value=[],
                id="year",
                multi=True, ),
            html.Br(),
        ]),

        dbc.Col(width=10, children=[
            dcc.Graph(id="radar_chart"),
        ]),
    ]),
])

app.layout = radar_page

@app.callback(
    Output("radar_chart", "figure"),
    [Input("country", "value")], [Input("year", "value")])

def update_chart(country, year):

    indicators_title = ['Time required score','Procedures required score','Cost (% of income per capita) score']
    country_list = df_radar['Country Name'].unique().tolist()

    # If nothing is chosen
    if len(country) == 0:
        country = ['Afghanistan']
    if len(year) == 0:
        year = [2020]

    # Get data
    year = ''.join(filter(str.isalnum, str(year)))
    country = ''.join(filter(str.isalnum, str(country)))
    header = df_radar.columns.tolist()
    col = header.index(year)
    row = country_list.index(country)
    radar_m = [df_radar.iloc[0+row, col], df_radar.iloc[382+row, col], df_radar.iloc[764+row, col]]
    radar_w = [df_radar.iloc[191+row, col], df_radar.iloc[573+row, col], df_radar.iloc[955+row, col]]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=radar_m,
        theta=indicators_title,
        line_color='blue',
        fill='toself',
        name=f'Men {df_radar.iloc[0+row, 0]}'
    ))

    fig.add_trace(go.Scatterpolar(
        r=radar_w,
        theta=indicators_title,
        line_color='red',
        fill='toself',
        name=f'Women {df_radar.iloc[0+row, 0]}'
    ))

    fig.update_layout(
        title= f'Scores for ease of setting up a business according to gender in {df_radar.iloc[0+row,0]}',
        polar=dict(
            radialaxis=dict(
            visible=True,
            range=[0, 100]
            )))

    fig.layout.autosize = True
    fig.update_layout(title=dict(font=dict(size=20)),
                      margin=dict(l=15, r=15, t=35, b=5),
                      autosize = True)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)