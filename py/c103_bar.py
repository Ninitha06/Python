import pandas as pd
import plotly.express as px


df = pd.read_csv("./csv/data.csv")

# fig = px.bar(df,x="Country",y="InternetUsers",color="Country")

# fig.show()

fig = px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60)
fig.show()