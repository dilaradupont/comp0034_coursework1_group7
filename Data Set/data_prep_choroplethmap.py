import pandas as pd


df = pd.read_csv('DBJoint.csv')


# Drop currency unit, Indicator code
df = df.drop(columns=['Currency Unit', 'Indicator Code'])

df = df.melt({'Country Name', 'Country Code', 'Urban Code', 'Urban Area Name', 'Region', 'Income Group',
              'Indicator Name'}, value_name='Score', var_name='Year') # add columns name to {} all but those starting in year


df = df[['Country Name', 'Country Code', 'Urban Code', 'Urban Area Name', 'Region', 'Income Group', 'Year', 'Indicator Name',
       'Score']]

df = df.pivot(index={'Country Name', 'Country Code', 'Urban Code', 'Urban Area Name', 'Region', 'Income Group', 'Year'},
              columns='Indicator Name', values='Score') # Add columns to country and year (all but Indicator Name and the one with the values)
df = df.reset_index()

df = df[['Country Name', 'Country Code', 'Urban Area Name', 'Urban Code', 'Region', 'Income Group', 'Year',
         'Starting a business - Score', 'Starting a business: Cost - Men (% of income per capita)',
         'Starting a business: Cost - Men (% of income per capita) - Score',
         'Starting a business: Cost - Women (% of income per capita)',
         'Starting a business: Cost - Women (% of income per capita) - Score',
         'Starting a business: Minimum capital (% of income per capita)',
         'Starting a business: Paid-in Minimum capital (% of income per capita) - Score',
         'Starting a business: Procedures required - Men (number)', 'Starting a business: Procedures required - Men (number) - Score',
         'Starting a business: Procedures required - Women (number)', 'Starting a business: Procedures required - Women (number) - Score',
         'Starting a business: Time - Men (days)', 'Starting a business: Time - Men (days) - Score', 'Starting a business: Time - Women (days)',
         'Starting a business: Time - Women (days)- Score']]

df = df.sort_values('Country Name') # Sort by alphabetical order on country column
df.to_csv('DBresorted_cm.csv', index=False)