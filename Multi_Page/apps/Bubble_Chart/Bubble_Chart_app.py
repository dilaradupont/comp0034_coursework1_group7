import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from IPython.display import display
from Multi_Page.StartingBusiness import app
import plotly.io as pio

pio.renderers.default = "browser"

''' THINGS TO DISCUSS
- Top of the page, select men, women, average
- selective legend -> done automatically
- how do we want to handle the case in which one of the parameters is 0? Right now we are removing it


TO DO:
- try implementing a bar at the bottom of this chart to select the different regions first
    if you can easily make that work, move on to implementing the plotly graph objects technique of clicking on dots
- add external border pink / blue
- add adaptive sizing
- remove everything but region, year, cost from hover label
- see if you can add trace 
'''


df_by_region = pd.read_csv('apps/Bubble_Chart/DBBubbleChart_Regional.csv')
df_general = pd.read_csv('apps/Bubble_Chart/DBBubbleChart.csv')


external_stylesheets = [dbc.themes.COSMO]
region_bubblechart_list = df_general['Region'].unique()

bubblechart_page = dbc.Container(fluid=True, children=[
    dbc.Row(
        dbc.Col(children=[html.Br()])),

    dbc.Row([
        dbc.Col(width=2, children=[
            html.Br(),
            html.H5("Select Gender"),
            dbc.Checklist(
                options=[
                    {"label": "Women", "value": 1},
                    {"label": "Men", "value": 2},
                ],
                value=[1, 2],
                id="gender",
                inline=True,
                switch=True,
                style={'margin': '20px'}
            ),
            html.H5("Select Region"),
            dcc.Dropdown(
                options=[{"label": x, "value": x}
                         for x in region_bubblechart_list],
                value=[],
                id="region",
                multi=True, ),
            html.Br(),
        ]),

        dbc.Col(width=10, children=[
            dcc.Graph(id="bubble_chart"),
        ]),
    ]),
])
app.layout = bubblechart_page


@app.callback(
    Output("bubble_chart", "figure"),
    [Input("gender", "value")], [Input("region", "value")])
def update_chart(gender, region):
    if gender == [1]:
        x_header = 'Time - Women (days)'
        y_header = 'Procedures required - Women (number)'
        size_header = 'Cost - Women (% of income per capita)'
        title_text = 'Elements involved in starting a business (Women)'
    elif gender == [2]:
        x_header = 'Time - Men (days)'
        y_header = 'Procedures required - Men (number)'
        size_header = 'Cost - Men (% of income per capita)'
        title_text = 'Elements involved in starting a business (Men)'
    else:
        x_header = 'Time - Average'
        y_header = 'Procedures required - Average'
        size_header = 'Cost - Average'
        title_text = 'Elements involved in starting a business (Average)'

    if not region:
        df = df_by_region
        hover_header = 'Region'
    else:
        df_averaged = df_general.loc[~(df_general['Region'].isin(region))].groupby(['Region', 'Year'],
                                                                                   as_index=False).mean()
        df = df_general.loc[df_general['Region'].isin(region)].append(df_averaged)
        df = df.dropna(subset=[x_header, y_header, size_header])
        df = df.loc[~((df[x_header] == 0) | (df[y_header] == 0) | (df[size_header] == 0))]  # drop countries that
        # cannot be represented in the chart because of a value = 0
        hover_header = 'Country Name'
        for r in range(
                len(df['Country Name'])):  # update the country name to match the region name for the averaged rows
            if pd.isnull(df['Country Name'].iloc[r]):
                df['Country Name'].iloc[[r]] = df['Region'].iloc[[r]]

    df = df.sort_values(
        by=['Region', 'Year'])  # this allows to maintain the color constant (and to not change the year)
    fig = px.scatter(df,
                     x=x_header,
                     y=y_header,
                     animation_frame='Year',
                     size=size_header,
                     color='Region',
                     range_x=[0, 100],
                     range_y=[0, 100],
                     hover_name=hover_header,
                     labels={x_header: 'Time [Score]',
                             y_header: 'Procedures required [Score]',
                             size_header: 'Cost [Score]'
                             },
                     title= title_text)
    if region:
        # if one specific region is selected to open up, slightly fade the markers at the back
        for year in df['Year'].unique():
            fig.for_each_trace(
                lambda trace: trace.update(marker={"opacity": 0.4}) if (trace.name not in region) else (),
            )

    fig.layout.autosize = True
    fig.update_layout(title=dict(font=dict(size=20)),
                      margin=dict(l=15, r=15, t=35, b=5),
                      autosize = True)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
