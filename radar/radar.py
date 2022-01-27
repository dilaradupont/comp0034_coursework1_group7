import pandas as pd
import plotly.graph_objects as go

df1 = pd.read_csv('Data Set/DBJoint.csv')
categories = ['Time required score','Procedures required score','Cost (% of income per capita) score']
fig = go.Figure()
indicator_list = ['IC.REG.DURS.MA.DY.DFRN', 'IC.REG.DURS.FE.DY.DRFN', 'IC.REG.PROC.FE.NO.DFRN',
 'IC.REG.PROC.MA.NO.DFRN', 'IC.REG.COST.PC.FE.ZS.DRFN', 'IC.REG.COST.PC.MA.ZS.DFRN']

# Modify dataframe 
df1 = df1[df1["Indicator Code"].isin(indicator_list)]
df1 = df1[['Country Name', 'Country Code', 'Indicator Name', 'Urban Area Name', 'Urban Code', 'Indicator Code', '2020']]
df1.reset_index(drop=True, inplace=True)
df1.to_csv('radar/radar_data.csv')

# Tracing first radar chart
radar_m = [df1.iloc[0, 6], df1.iloc[2, 6], df1.iloc[5, 6]]
radar_w = [df1.iloc[3, 6], df1.iloc[1, 6], df1.iloc[4, 6]]

fig.add_trace(go.Scatterpolar(
    r=radar_m,
    theta=categories,
    fill='toself',
    name=f'Men {df1.iloc[0, 0]}'
))
fig.add_trace(go.Scatterpolar(
    r=radar_w,
    theta=categories,
    fill='toself',
    name=f'Women {df1.iloc[0, 0]}'
))

# Adding other charts
for i in range(6):
    radar_m = [df1.iloc[0+6*i, 6], df1.iloc[2+i, 6], df1.iloc[5+6*i, 6]]
    radar_w = [df1.iloc[3+6*i, 6], df1.iloc[1, 6], df1.iloc[4+6*i, 6]]

    fig.update_traces(go.Scatterpolar(
        r=radar_m,
        theta=categories,
        fill='toself',
        name=f'Men {df1.iloc[0+6*i, 0]}'
    ))
    fig.add_trace(go.Scatterpolar(
        r=radar_w,
        theta=categories,
        fill='toself',
        name=f'Women {df1.iloc[0+6*i, 0]}'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 100]
        )),
    showlegend=False
    )

    fig.show()

