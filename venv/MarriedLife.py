import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("Data/mafs.csv")
print(df.info())

# --------------------------- SIMPLE BAR CHART - Region  --------------------------------------
# grs = df.groupby(["Location"])[["Decision"]].count().reset_index()
#
# fig = px.bar(grs,
#              x='Decision',
#              y='Location',
#              title='Test',
#              color='Decision',
#              barmode='stack'
#              )
# --------------------------- SIMPLE BAR CHART(2) - Region  --------------------------------------
grs = df.groupby(["Age"])[["Decision"]].count().reset_index()
a = df.loc[df['Decision']=='Yes'].agg(['count'])
b = df.loc[df['Decision']=='No'].agg(['count'])

fig = px.bar(grs,
             x='Age',
             y= a/b,
             title='Test',
             color='Decision',
             barmode='stack'
             )
# --------------------------- STACKED BAR CHART - Region  --------------------------------------
# grgs = df.groupby(["Sex","Ethnicity"])[["Attainment8"]].mean().reset_index()
# fig = px.bar(grgs,
#              x="Sex",
#              y="Attainment8",
#              color='Ethnicity',
#              barmode='stack')
fig.show()