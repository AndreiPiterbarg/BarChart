import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("Data/gcse-results-ethnicity (1).csv")
print(df.info())
print(df.Year.unique())

df['Attainment8'].replace('x','0',inplace=True)
df['Attainment8'].replace('.','0',inplace=True)
df['Sex'].replace('Girls ','Girls',inplace=True)
df['Ethnicity'].replace('Asian ','Asian',inplace=True)
df['Ethnicity'].replace('Black ','Black',inplace=True)
df['Ethnicity'].replace('White ','White',inplace=True)
# df['Attainment8'].replace('x','0',inplace=True)
# df['Attainment8'].replace('x','0',inplace=True)

df.loc[df['Attainment8']== 'x']

df.Attainment8 = df.Attainment8.astype(float)


# df.Attainment8 = df.Attainment8.astype(float).fillna(0.0)
# df.Attainment8 = df.Attainment8.round()
# --------------------------- SIMPLE BAR CHART - Region  --------------------------------------
# grs = df.groupby(["Year"])[["Attainment8"]].mean().reset_index()

# fig = px.bar(grs,
#              x='Year',
#              y="Attainment8",
#              title='Test',
#              color='Year',
#              barmode='stack'
#              )
# --------------------------- STACKED BAR CHART - Region  --------------------------------------
grgs = df.groupby(["Sex","Ethnicity"])[["Attainment8"]].mean().reset_index()
fig = px.bar(grgs,
             x="Sex",
             y="Attainment8",
             color='Ethnicity',
             barmode='stack')
fig.show()
