import plotly.express as px
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd

''' THINGS TO DISCUSS
- Top of the page, select men, women, average
- When you click on a bubble you can see the dots for countries within that region
- selective legend
- what range to set for the x and y axis
'''

df_by_region = pd.read_csv('./Data Set/DBBubbleChart_Regional.csv')
df = pd.read_csv('./Data Set/DBBubbleChart.csv')

external_stylesheets = [dbc.themes.COSMO]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# gender_bubblechart_list = ['Women', 'Men']

app.layout = html.Div([
    html.Div([dbc.Label("Gender:"),  # create the tick-box at the top to distinguish between men and women
              dbc.Checklist(
                  options=[
                      {"label": "Women", "value": 1},
                      {"label": "Men", "value": 2},
                  ],
                  value=[],
                  id="gender_selection",
                  inline=True,
                  switch=True,
              ),
              dcc.Graph(id="bubble_chart")
              ])
])


@app.callback(
    Output("bubble_chart", "figure"),
    Input("gender_selection", "value"),
)
def update_chart(gender_selection):
    if gender_selection == [1]:
        x_header = 'Time - Women (days)'
        y_header = 'Procedures required - Women (number)'
        size_header = 'Cost - Women (% of income per capita)'
    elif gender_selection == [2]:
        x_header = 'Time - Men (days)'
        y_header = 'Procedures required - Men (number)'
        size_header = 'Cost - Men (% of income per capita)'
    else:
        x_header = 'Time - Average'
        y_header = 'Procedures required - Average'
        size_header = 'Cost - Average'

    fig = px.scatter(df_by_region, x=x_header, y=y_header, animation_frame='Year',
                     size=size_header, color='Region', range_x=[20, 100], range_y=[20, 100])
    return fig

'''fig_BC_reg = px.scatter(df_by_region, x='Time - Average', y='Procedures required - Average', animation_frame='Year',
                      size='Cost - Average', color='Region', range_x=[20, 100], range_y=[20,100])'''

if __name__ == '__main__':
    app.run_server(debug=True)
