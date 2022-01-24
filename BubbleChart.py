# any figure created using plotly can be displayed on a Dash App using the graph component
# instructions from: https://plotly.com/python/bubble-charts/
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
"""

import plotly.express as px
import pandas as pd
from IPython.display import display


def separate_column(df, column_header, column_with_duplicates, column_with_value):
    unique_values = df[column_header].unique().tolist()
    df_copy = df
    df = df.drop_duplicates(subset=[column_with_duplicates])
    for index in range(len(unique_values)):
        column_values = df_copy[df_copy[column_header] == unique_values[index]]
        df[unique_values[index]] = column_values[column_with_value].tolist()
    df = df.drop(columns=[column_header, column_with_value])
    return df


df = pd.read_csv('./Data Set/DBJoint.csv')

# clean data to remove all unnecessary rows
row = 0

# Get columns name, drop currency unit, Indicator code and move region and income group to front
# df = df.drop(columns=['Currency Unit', 'Indicator Code'])

genders, indicator = ([] for l in range(2))
for value in df['Indicator Name']:
    if 'Score' not in value or ('Time' not in value and 'Procedures' not in value and 'Cost' not in value):
        df = df.drop([row])
        if 'Women' in value:
            genders.append('W')
            split_value = value.split('-', 1)
            indicator.append(split_value[0].replace('Starting a business: ', '').strip())
        elif 'Men' in value:
            genders.append('M')
            split_value = value.split('-', 1)
            indicator.append(split_value[0].replace('Starting a business: ', '').strip())
    row = row + 1
df = df.drop(columns=['Indicator Name', 'Indicator Code', 'Country Code', 'Urban Area Name', 'Urban Code',
                      'Currency Unit'])
df['Indicator Name'] = indicator
df['Gender'] = genders

df = df.melt({'Country Name', 'Region', 'Income Group', 'Indicator Name', 'Gender'}, value_name='Score',
             var_name='Year')
df = df[['Country Name', 'Region', 'Income Group', 'Gender', 'Year', 'Indicator Name', 'Score']]
df_piv = df.pivot_table(values='Score', index=df.index, columns='Indicator Name', aggfunc='first')
df = df.reset_index()
df_piv = df_piv.reset_index()
df = pd.merge(df, df_piv)
df = df.groupby(['Country Name', 'Region', 'Income Group', 'Gender', 'Year'], as_index=False).agg({'Time': 'sum',
                                                                                                   'Cost': 'sum',
                                                                                                   'Procedures required': 'sum'})
df_by_region = df.groupby(['Region', 'Year'], as_index=False).mean()
fig = px.scatter(df_by_region, x='Time', y='Procedures required', color='Region', size='Cost', animation_frame='Year',
                 title='Cost of starting a business (Score) as a function of time, procedures required, and region',
                 labels={'Time': 'Time required to start a business - score',
                         'Procedures required': 'Procedures required to start a business - score',
                         'Region': 'Geographical region', 'Cost': 'Cost to start a business - score'})
fig.update_xaxes(range=[0, 200])
fig.update_yaxes(range=[0, 200])

fig.show()

# df_by_region.to_csv('data_cleaned.csv', index=False)
# df_piv.to_csv('data_cleaned_time.csv', index=False)
# df_by_region.to_csv('data_cleaned_by_region.csv', index=False)


# Calculate Average - CHANGE WAY HEADERS ARE FOUND
# headers_to_drop = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
#                   '2018', '2019', '2020', 'Indicator Code', 'Currency Unit']


# df['Average'] = df.mean(axis=1, skipna=True, numeric_only=True)
# df = df.drop(columns=headers_to_drop, axis=0)
# for one region, take the average of all the same indicators - across the years and across countries
# df_by_region = df.groupby(['Region', 'Indicator Name'], as_index=False).mean()

# unique_indicators = df_by_region['Indicator Name'].unique().tolist()
# df_by_region = separate_column(df_by_region, 'Indicator Name', 'Region', 'Average')

# fig_by_region = px.scatter(df_by_region, x='Time ', y='Procedures required ', color='Region', size='Cost ')
