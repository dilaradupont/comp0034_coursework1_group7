import pandas as pd

df = pd.read_csv('./DBJoint.csv')

# Remove all rows that are not Time, Cost, Procedures required - Score
indicator_codes_list = ['IC.REG.COST.PC.MA.ZS.DFRN', 'IC.REG.COST.PC.FE.ZS.DRFN', 'IC.REG.PROC.MA.NO.DFRN',
                        'IC.REG.PROC.FE.NO.DFRN', 'IC.REG.DURS.MA.DY.DFRN', 'IC.REG.DURS.FE.DY.DRFN',
                        'IC.REG.COST.PC.MA.ZS', 'IC.REG.COST.PC.FE.ZS', 'IC.REG.PROC.MA.NO',
                        'IC.REG.PROC.FE.NO', 'IC.REG.DURS.MA.DY', 'IC.REG.DURS.FE.DY']

df = df[df['Indicator Code'].isin(indicator_codes_list)]
# Remove 'Starting a Business' and "-Score" from indicator name
df['Indicator Name'] = df['Indicator Name'].str.replace("Starting a business: ", "")
df['Indicator Name'] = df['Indicator Name'].str.strip()

df = df.drop(columns=['Currency Unit', 'Indicator Code'])

# Create one row per year
df = df.melt({'Country Name', 'Country Code', 'Urban Code', 'Urban Area Name', 'Region', 'Income Group',
              'Indicator Name'}, value_name='Score', var_name='Year')
df = df[['Country Name', 'Country Code', 'Urban Code', 'Urban Area Name', 'Region', 'Income Group', 'Year',
         'Indicator Name',
         'Score']]

# Turn the indicator column into one column per indicator
df = df.pivot(index={'Country Name', 'Country Code', 'Urban Code', 'Urban Area Name', 'Region', 'Income Group', 'Year'},
              columns='Indicator Name', values='Score')
df = df.reset_index()
df = df[df['Urban Code'].isnull()]
df = df.drop(columns=['Country Code', 'Urban Area Name', 'Urban Code'])

# Create an average of the indicators
df['Cost (Average) - Score'] = df[['Cost - Men (% of income per capita) - Score', 'Cost - Women (% of income per '
                                                                                  'capita) - Score']].mean(axis=1)
df['Procedures required (Average) - Score'] = df[[
    'Procedures required - Men (number) - Score', 'Procedures required - Women (number) - Score']].mean(axis=1)
df['Time (Average) - Score'] = df[['Time - Men (days) - Score', 'Time - Women (days)- Score']].mean(axis=1)

df['Cost (Average)'] = df[['Cost - Men (% of income per capita)', 'Cost - Women (% of income per capita)']].mean(axis=1)
df['Procedures required (Average)'] = df[[
    'Procedures required - Men (number)', 'Procedures required - Women (number)']].mean(axis=1)
df['Time (Average)'] = df[['Time - Men (days)', 'Time - Women (days)']].mean(axis=1)

df.to_csv('DBBubbleChart.csv', index=False)
