import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

df = pd.read_csv("Data/mafs.csv")


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
# # --------------------------- SIMPLE BAR CHART(2) - Region  --------------------------------------
# grs = df.groupby(["Location","Decision"])[["Decision"]].size().reset_index(name='Yes')
# grs_participants = df.groupby(["Location"])[["Decision"]].size().reset_index(name='Participants_qt')
#
# grs_yes = grs[grs['Decision']=='Yes']
#
# grs_yes.set_index('Location', inplace=True)
# grs_participants.set_index('Location', inplace=True)
#
# grs_yes["ratio"] = grs_yes["Yes"]/grs_participants["Participants_qt"]
#
# grs_yes.reset_index(inplace = True)
#
# fig = px.bar(grs_yes,
#              x='Location',
#              y= 'ratio',
#              title='Test',
#              color='Location',
#              barmode='stack'
#              )
# --------------------------- IMPOSSIBLE BAR CHART(3) - Region  --------------------------------------
# grs = df.groupby(["Age","Decision"])[["Decision"]].size().reset_index(name='Yes')
# grs_participants = df.groupby(["Age"])[["Decision"]].size().reset_index(name='Participants_qt')
#
# grs_yes = grs[grs['Decision']=='Yes']
#
# grs_yes.set_index('Age', inplace=True)
# grs_participants.set_index('Age', inplace=True)
#
# grs_yes["ratio"] = grs_yes["Yes"]/grs_participants["Participants_qt"]
#
# grs_yes.reset_index(inplace = True)
#
# print(grs_yes)
#
# fig = px.bar(grs_yes,
#              x='Age',
#              y= 'ratio',
#              title='Test',
#              color='Age',
#              barmode='stack'
#              )

# --------------------------- IMPOSSIBLE BAR CHART(3) - Region  --------------------------------------
grs = df.groupby(["Decision"])[["Decision"]].size().reset_index(name='Yes')
grs_married = df.groupby(["Status"])[["Decision"]].size().reset_index(name='StillMarried')

grs_yes = grs[grs['Decision']=='Yes']
grs_married = grs_married[grs_married['Status']=='Married']

grs_yes["ratio"] = grs_married["StillMarried"]/grs_yes["Yes"]

print(grs_yes)

