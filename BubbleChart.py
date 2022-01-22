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

df = pd.read_csv('./Data Set/DBJoint.csv')

# clean data to remove all unnecessary rows
row = 0
genders, indicator = ([] for l in range(2))
for value in df['Indicator Name']:
    if 'Score' not in value or ('Time' not in value and 'Procedures' not in value and 'Cost' not in value):
        df = df.drop([row])
        if 'Women' in value:
            genders.append('W')
            split_value = value.split('-', 1)
            indicator.append(split_value[0].replace('Starting a business: ', ''))
        elif 'Men' in value:
            genders.append('M')
            split_value = value.split('-', 1)
            indicator.append(split_value[0].replace('Starting a business: ', ''))
        '''else:
            genders.append('U')
            split_value = value.split('-', 1)
            indicator.append(split_value[0].replace('Starting a business: ', ''))'''
    row = row + 1
df = df.drop(columns=['Indicator Name'])
df['Indicator Name'] = indicator
df['Gender'] = genders

# Calculate Average -CHANGE WAY HEADERS ARE FOUND
headers_to_drop = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017',
                   '2018', '2019', '2020', 'Indicator Code', 'Currency Unit']

# Issue: columns with value of 0, should we consider them?
df['Average'] = df.mean(axis=1, skipna=True, numeric_only=True)
df = df.drop(columns=headers_to_drop, axis=0)
# for one region, take the average of all the same indicators - across the years and across countries

df_by_region = df.groupby(['Region', 'Indicator Name'], as_index=False).mean()

unique_indicators = df_by_region['Indicator Name'].unique().tolist()
df_time = df_by_region[df_by_region['Indicator Name'] == unique_indicators[0]]
df_time = df_time['Average']
display(df_time)

df_cost = df_by_region[df_by_region['Indicator Name'] == unique_indicators[1]]
df_cost = df_cost['Average']
display(df_cost)

df_procedure = df_by_region[df_by_region['Indicator Name'] == unique_indicators[2]]
df_procedure = df_procedure['Average']
display(df_procedure)

df_by_region = df_by_region.drop_duplicates(subset=['Region'])
df_by_region['Cost'] = df_cost.tolist()
df_by_region['Time'] = df_time.tolist()
df_by_region['Procedure'] = df_procedure.tolist()

# fig = px.scatter(df_by_region, x = df[df_by_region['Indicator Name'] == 'Time'], y = [df_by_region['Indicator Name'] == 'Cost'])
df.to_csv('data_cleaned.csv', index=False)
df_by_region.to_csv('data_cleaned_by_region.csv', index=False)