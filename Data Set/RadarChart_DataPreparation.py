import pandas as pd

df = pd.read_csv('DBJoint.csv')

# print(df['Indicator Name'].value_counts())

indicators_title = ['Time required score', 'Procedures required score', 'Cost (% of income per capita) score']
indicator_code = ['IC.REG.DURS.MA.DY.DFRN', 'IC.REG.DURS.FE.DY.DRFN', 'IC.REG.PROC.MA.NO.DFRN',
                  'IC.REG.PROC.FE.NO.DFRN',
                  'IC.REG.COST.PC.MA.ZS.DFRN', 'IC.REG.COST.PC.FE.ZS.DRFN']

# Modify dataframe 
df = df[df['Indicator Code'].isin(indicator_code)]
df['Urban Area Name'].fillna(0, inplace=True)
df.drop(df.loc[df['Urban Area Name'] != 0].index, inplace=True)
df.drop(['Urban Area Name', 'Urban Code', 'Currency Unit', 'Region', 'Income Group'], axis=1, inplace=True)
df.reset_index(drop=True, inplace=True)

# Reorder dataframe
data = []
for i in range(len(indicator_code)):
    df1 = df[df['Indicator Code'] == indicator_code[i]]
    data.append(df1)

df_radar = pd.concat([data[0], data[1], data[2], data[3], data[4], data[5]], axis=0, join="outer")
df.reset_index(drop=True, inplace=True)

df_radar.to_csv('DBRadar.csv', index=False)
