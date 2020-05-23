import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("Data/gcse-results-ethnicity (1).csv")
print(df.info())
print(df.Year.unique())

df['Attainment8'] = df['Attainment8'].str.replace('.',',')


# df['Attainment8'] = df['Attainment8'].astype(float)
df.Attainment8 = df.Attainment8.astype(float).fillna(0.0)
df.Attainment8 = df.Attainment8.round()
grs = df.groupby(["Sex"])[["Attainment8"]].mean().reset_index()

fig = px.bar(grs,
             x='Sex',
             y="Attainment8",
             title='Test',
             color='status',
             barmode='stack'
             )

fig.show()