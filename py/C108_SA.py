import pandas as pd
import plotly.figure_factory as ff


df = pd.read_csv('./csv/HeightWeight.csv')

fig = ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)

#The y-axis in a dist plot is the probability density function for the kernel density estimation. 
# so y axis is 0.05 means 5% has this height
#show_hist true means shows bar plots also...
fig1 = ff.create_distplot([df["Weight(Pounds)"].tolist()],["Weight"],show_hist=True)

fig.show()

fig1.show()

