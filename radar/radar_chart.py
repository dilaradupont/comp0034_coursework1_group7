import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('radar/radar_data.csv')
print(df['Indicator Name'].value_counts())
indicators_title = ['Time required score','Procedures required score','Cost (% of income per capita) score']
indicator_code = ['IC.REG.DURS.MA.DY.DFRN', 'IC.REG.DURS.FE.DY.DRFN', 'IC.REG.PROC.MA.NO.DFRN', 'IC.REG.PROC.FE.NO.DFRN',
 'IC.REG.COST.PC.MA.ZS.DFRN', 'IC.REG.COST.PC.FE.ZS.DRFN']

# Tracing first radar chart
fig = go.Figure()
x = 185
year_col = 5

radar_m = [df.iloc[0+x, year_col], df.iloc[382+x, year_col], df.iloc[764+x, year_col]]
radar_w = [df.iloc[191+x, year_col], df.iloc[573+x, year_col], df.iloc[955+x, year_col]]

fig.add_trace(go.Scatterpolar(
    r=radar_m,
    theta=indicators_title,
    line_color='blue',
    fill='toself',
    name=f'Men {df.iloc[0+x, 0]}'
))

fig.add_trace(go.Scatterpolar(
    r=radar_w,
    theta=indicators_title,
    line_color='red',
    fill='toself',
    name=f'Women {df.iloc[0+x, 0]}'
))

fig.update_layout(
    title= f'Scores for ease of setting up a business according to gender in {df.iloc[0+x,0]} based on different indicators',
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 100]
        )))

fig.show()

# import plotly.graph_objects as go # or plotly.express as px
# fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# # fig.add_trace( ... )
# # fig.update_layout( ... )

# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     dcc.Graph(figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

# # Adding other charts
# for i in range(1):
#     radar_m = [df1.iloc[0+*i, 5], df1.iloc[2+i*5, 5], df1.iloc[5+5*i, 5]]
#     radar_w = [df1.iloc[3+5*i, 5], df1.iloc[1, 5], df1.iloc[4+5*i, 5]]

#     fig.update_traces(go.Scatterpolar(
#         r=radar_m,
#         theta=categories,
#         fill='toself',
#         name=f'Men {df1.iloc[0+6*i, 0]}'
#     ))
#     fig.add_trace(go.Scatterpolar(
#         r=radar_w,
#         theta=categories,
#         fill='toself',
#         name=f'Women {df1.iloc[0+6*i, 0]}'
#     ))

#     fig.update_layout(
#     polar=dict(
#         radialaxis=dict(
#         visible=True,
#         range=[0, 100]
#         )),
#     showlegend=False
#     )

#     fig.show()