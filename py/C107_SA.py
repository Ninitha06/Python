import pandas as pd

import plotly.graph_objects as go

df = pd.read_csv('./csv/pixelMath.csv')

#indexing in the data frame formed by pd is numbers starting from 0. Hence can't use student id directly. 
# It has to be written as a condition
print(df.loc[8])

studentDetail = df.loc[df['student_id']=='TRL_987']
print(studentDetail)

fig = go.Figure(go.Bar(
    x=studentDetail.groupby("level")["attempt"].mean(),
    y=["Level 1","Level 2","Level 3","Level 4"],
    orientation='h'))


fig.show()