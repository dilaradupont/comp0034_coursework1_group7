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
        dbc.Col(width=6, children=[
            dcc.Graph(id="radar_chart"),
        ]),
        dbc.Col(width=6, children=[
            dcc.Graph(id="radar_chart1"),
        ]),
    ]),

    dbc.Row([
        dbc.Col(width={"size":3, "offset": 1}, children=[
            html.Br(),
            html.H5('Select Country'),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in country_list],
                value=[],
                id="country",
                multi=False, 
            ),
            html.H5('Select Year'),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in year_list],
                value=[],
                id="year",
                multi=False,
            ),
            html.Br(),
        ]),
        dbc.Col(width={"size":3, "offset": 3}, children=[
            html.Br(),
            html.H5('Select Country'),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in country_list],
                value=[],
                id="country1",
                multi=False,
            ),
            html.H5('Select Year'),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in year_list],
                value=[],
                id="year1",
                multi=False,
            ),
            html.Br(),
        ]),
    ]),
])

app.layout = radar_page

@app.callback(
    [Output("radar_chart", "figure"), Output("radar_chart1", "figure")],
    [Input("country", "value")], [Input("year", "value")], [Input("country1", "value")], [Input("year1", "value")])
def update_chart(country, year, country1, year1):
    # if len(country) == 0:
    #     country = ['Afghanistan']
    # if len(year) == 0:
    #     year = ['2020']

    # if len(country1) == 0:
    #     country1 = ['Afghanistan']
    # if len(year1) == 0:
    #     year1 = ['2019']

    if country == '':
        country = 'Afghanistan'
    if year == '':
        year = '2019'
    if year1 == '':
        year1 = '2019'
        year1 = '20'

    lis1 = [str(country), str(country1)]
    lis2 = [str(year), str(year1)]
    print(country)

    indicators_title = ['Time required score','Procedures required score','Cost (% of income per capita) score']
    country_list = df_radar['Country Name'].unique().tolist()
    lis_fig = []

    for i in range(len(lis1)):
        # Get data
        # year = ''.join(filter(str.isalnum, str(lis2[i])))
        # country = ''.join(filter(str.isalnum, str(lis1[i])))
        year = lis2[i]
        country = lis1[i]

        # Default graph settings
        # if country == '':
        #     country = 'Afghanistan'
        # if year == '' and i == 0:
        #     year = '2019'
        # if year == '' and i == 1:
        #     year = '2020'

        header = df_radar.columns.tolist()
        col = header.index(year)
        row = country_list.index(country)
        afg_idx = df_radar.index[df_radar['Country Name'] == df_radar.iloc[0, 0]].tolist()

        radar_m = [df_radar.iloc[afg_idx[0]+row, col], df_radar.iloc[afg_idx[2]+row, col], df_radar.iloc[afg_idx[4]+row, col]]
        radar_w = [df_radar.iloc[afg_idx[1]+row, col], df_radar.iloc[afg_idx[3]+row, col], df_radar.iloc[afg_idx[5]+row, col]]

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
            title= f'Scores for setting up a business according to gender in {df_radar.iloc[0+row,0]} in {header[col]}',
            polar=dict(
                radialaxis=dict(
                visible=True,
                range=[0, 100]
                )))

        fig.layout.autosize = True
        lis_fig.append(fig)

    return lis_fig[0], lis_fig[1]


if __name__ == '__main__':
    app.run_server(debug=True)