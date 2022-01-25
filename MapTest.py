
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
df = pd.read_csv('Data Set/DBresorted_cm.csv')
#---------------------------------------------------------------
app.layout = html.Div([

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    html.Div([
        dcc.Input(id='input_state', type='number', inputMode='numeric', value=2006,
                  max=2020, min=2006, step=1, required=True),
        html.Button(id='submit_button', n_clicks=0, children='Submit'),
        html.Div(id='output_state'),
    ],style={'text-align': 'center'}),

])

#---------------------------------------------------------------
@app.callback(
    [Output('output_state', 'children'),
    Output(component_id='the_graph', component_property='figure')],
    [Input(component_id='submit_button', component_property='n_clicks')],
    [State(component_id='input_state', component_property='value')]
)

def update_output(num_clicks, val_selected):
    if val_selected is None:
        raise PreventUpdate
    else:
        df = pd.read_csv('Data Set/DBresorted_cm.csv').query("Year=={}".format(val_selected))
        # print(df[:3])

        fig = px.choropleth(df, locations="Country Code",
                            color="Starting a business - Score",
                            hover_name="Country Name",
                            projection='natural earth',
                            title='Starting a business - Score by Year',
                            color_continuous_scale=px.colors.sequential.Plasma)

        fig.update_layout(title=dict(font=dict(size=28),x=0.5,xanchor='center'),
                          margin=dict(l=250, r=10, t=50, b=50))

        return ('The input value was "{}" and the button has been \
                clicked {} times'.format(val_selected, num_clicks), fig)

if __name__ == '__main__':
    app.run_server(debug=True)