from os import stat
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

df = pd.read_csv('./csv/interventions_data/School2.csv')
# df = pd.read_csv('./csv/studentMarks.csv')
data = df["Math_score"].tolist()

# fig1 = ff.create_distplot([data],["Math Scores"],show_hist=False)
# fig1.show()

mean_population = statistics.mean(data)
stddev_population = statistics.stdev(data)

print("Mean of population " ,mean_population)
print("Std deviation of population ",stddev_population)

def mean_of_samples():
    sample_array = []
    for i in range(0,100):
        random_index = random.randint(0,len(data)-1)
        random_sample = data[random_index]
        sample_array.append(random_sample)
    mean = statistics.mean(sample_array)
    return mean

mean_list = []
for i in range(0,1000):
    sample_mean = mean_of_samples()
    mean_list.append(sample_mean)

mean_sampling = statistics.mean(mean_list)
stddev_sampling = statistics.stdev(mean_list)

print("Mean of sampling ",mean_sampling)
print("Std deviation of sampling ",stddev_sampling)

# fig2 = ff.create_distplot([mean_list],["Math marks Sampled"],show_hist=False)
# fig2.add_trace(go.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.20],mode="lines",name="MEAN"))
# fig2.show()

first_std_dev_start,first_std_dev_end = mean_sampling-stddev_sampling,mean_sampling+stddev_sampling
second_std_dev_start,second_std_dev_end = mean_sampling-(2*stddev_sampling),mean_sampling+(2*stddev_sampling)
third_std_dev_start,third_std_dev_end = mean_sampling-(3*stddev_sampling),mean_sampling+(3*stddev_sampling)

print("std1",first_std_dev_start,first_std_dev_end)
print('std2',second_std_dev_start,second_std_dev_end)
print("std3",third_std_dev_start,third_std_dev_end)

# df_data1 = pd.read_csv("./csv/data1.csv")
df_data1 = pd.read_csv("./csv/interventions_data/School_2_Sample.csv")
data1 = df_data1["Math_score"].tolist()

mean_sample1 = statistics.mean(data1)
print("Sample 1 Mean", mean_sample1)

# df_data2 = pd.read_csv("./csv/data2.csv")
# data2 = df_data2["Math_score"].tolist()

# mean_sample2 = statistics.mean(data2)
# print("Sample 2 Mean", mean_sample2)

# df_data3 = pd.read_csv("./csv/data3.csv")
# data3 = df_data3["Math_score"].tolist()

# mean_sample3 = statistics.mean(data3)
# print("Sample 3 Mean", mean_sample3)

fig3 = ff.create_distplot([mean_list],["Students Marks"],show_hist=False)
fig3.add_trace(go.Scatter(x=[mean_sampling,mean_sampling],y=[0,0.17],mode="lines",name="MEAN_SAMPLING"))
fig3.add_trace(go.Scatter(x=[mean_sample1,mean_sample1],y=[0,0.17],mode="lines+markers",name="MEAN SAMPLE1"))
# fig3.add_trace(go.Scatter(x=[mean_sample2,mean_sample2],y=[0,0.17],mode="lines+markers",name="MEAN SAMPLE2"))
# fig3.add_trace(go.Scatter(x=[mean_sample3,mean_sample3],y=[0,0.17],mode="lines+markers",name="MEAN SAMPLE3"))
fig3.add_trace(go.Scatter(x=[first_std_dev_start,first_std_dev_start],y=[0,0.17],mode="lines",name="STD DEV 1 START"))
fig3.add_trace(go.Scatter(x=[first_std_dev_end,first_std_dev_end],y=[0,0.17],mode="lines",name="STD DEV 1 END"))
fig3.add_trace(go.Scatter(x=[second_std_dev_start,second_std_dev_start],y=[0,0.17],mode="lines",name="STD DEV 2 START"))
fig3.add_trace(go.Scatter(x=[second_std_dev_end,second_std_dev_end],y=[0,0.17],mode="lines",name="STD DEV 2 END"))
fig3.add_trace(go.Scatter(x=[third_std_dev_start,third_std_dev_start],y=[0,0.17],mode="lines",name="STD DEV 3 START"))
fig3.add_trace(go.Scatter(x=[third_std_dev_end,third_std_dev_end],y=[0,0.17],mode="lines",name="STD DEV 3 END"))
fig3.show()


z_score = (mean_sample1-mean_sampling)/stddev_sampling
print("Z score",z_score)