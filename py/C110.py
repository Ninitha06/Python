from itertools import count
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random


df = pd.read_csv("./csv/average.csv")

#data = df["temp"].tolist() - TA
data = df["average"].tolist()
population_mean = statistics.mean(data)
population_stdDev = statistics.stdev(data)

print("Population Mean :- ",population_mean)
print("Population Std dev :- ",population_stdDev)
 
#fig = ff.create_distplot([data],["temp"],show_hist=False) - TA
fig = ff.create_distplot([data],["Average"],show_hist=False)
#fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,0.1],mode="lines",name="MEAN")) - TA
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,1.5],mode="lines",name="MEAN"))
fig.show()

def showFig(data_list):
    #fig = ff.create_distplot([data_list],["temp"],show_hist=False) - TA
    fig = ff.create_distplot([data_list],["Average"],show_hist=False)
    fig.show()

def random_samples_mean(counter):
    dataset=[]
    for i in range(0,counter):
        # to avoid index out of range, len(data)-1
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
   # showFig(dataset)
    return mean

# 100 is the sampling size
samples_mean = random_samples_mean(100)

def random_from_mean_list():
    mean_list = []
    for i in range(0,1000):
        mean_val = random_samples_mean(100)
        mean_list.append(mean_val)
    showFig(mean_list)
    print("Sampling Mean :- ", str(statistics.mean(mean_list)))
    print("Sampling Std Dev :- ", str(statistics.stdev(mean_list)))

random_from_mean_list()






