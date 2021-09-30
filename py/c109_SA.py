from os import stat
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("./csv/HeightWeight.csv")

height_list = df["Height(Inches)"].tolist()
weight_list = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

print("The mean, median and mode of the height list are {},{},{}".format(height_mean,height_median,height_mode))
print("The mean, median and mode of the weight list are {},{},{}".format(weight_mean,weight_median,weight_mode))

height_StdDev = statistics.stdev(height_list)
weight_StdDev = statistics.stdev(weight_list)

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values

height_first_std_dev_start, height_first_std_dev_end = height_mean-height_StdDev,height_mean+height_StdDev
height_second_std_dev_start, height_second_std_dev_end = height_mean-(2*height_StdDev),height_mean+(2*height_StdDev)
height_third_std_dev_start, height_third_std_dev_end = height_mean-(3*height_StdDev),height_mean+(3*height_StdDev)

weight_first_std_dev_start, weight_first_std_dev_end = weight_mean-weight_StdDev,weight_mean+weight_StdDev
weight_second_std_dev_start, weight_second_std_dev_end = weight_mean-(2*weight_StdDev),weight_mean+(2*weight_StdDev)
weight_third_std_dev_start, weight_third_std_dev_end = weight_mean-(3*weight_StdDev),weight_mean+(3*weight_StdDev)

#Number of elements in each list

height_list_first_dev = [result for result in height_list if result>height_first_std_dev_start and result<height_first_std_dev_end]
height_list_second_dev = [result for result in height_list if result>height_second_std_dev_start and result<height_second_std_dev_end]
height_list_third_dev = [result for result in height_list if result>height_third_std_dev_start and result<height_third_std_dev_end]

weight_list_first_dev = [result for result in weight_list if result>weight_first_std_dev_start and result<weight_first_std_dev_end]
weight_list_second_dev = [result for result in weight_list if result>weight_second_std_dev_start and result<weight_second_std_dev_end]
weight_list_third_dev = [result for result in weight_list if result>weight_third_std_dev_start and result<weight_third_std_dev_end]

print("{}% of height data lies in first std deviation".format(len(height_list_first_dev)*100/len(height_list)))
print("{}% of height data lies in second std deviation".format(len(height_list_second_dev)*100/len(height_list)))
print("{}% of height data lies in third std deviation".format(len(height_list_third_dev)*100/len(height_list)))
print("{}% of weight data lies in first std deviation".format(len(weight_list_first_dev)*100/len(height_list)))
print("{}% of weight data lies in second std deviation".format(len(weight_list_second_dev)*100/len(height_list)))
print("{}% of weight data lies in third std deviation".format(len(weight_list_third_dev)*100/len(height_list)))


#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig = ff.create_distplot([height_list], ["Height"], show_hist=False)
fig.add_trace(go.Scatter(x=[height_mean, height_mean], y=[0, 0.22], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[height_first_std_dev_start, height_first_std_dev_start], y=[0, 0.125], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[height_first_std_dev_end, height_first_std_dev_end], y=[0, 0.125], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[height_second_std_dev_start, height_second_std_dev_start], y=[0, 0.06], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[height_second_std_dev_end, height_second_std_dev_end], y=[0, 0.06], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

fig1 = ff.create_distplot([weight_list], ["Weight"], show_hist=False)
fig1.add_trace(go.Scatter(x=[weight_mean, weight_mean], y=[0, 0.035], mode="lines", name="MEAN"))
fig1.add_trace(go.Scatter(x=[weight_first_std_dev_start, weight_first_std_dev_start], y=[0, 0.02], mode="lines", name="STANDARD DEVIATION 1"))
fig1.add_trace(go.Scatter(x=[weight_first_std_dev_end, weight_first_std_dev_end], y=[0, 0.02], mode="lines", name="STANDARD DEVIATION 1"))
fig1.add_trace(go.Scatter(x=[weight_second_std_dev_start, weight_second_std_dev_start], y=[0, 0.005], mode="lines", name="STANDARD DEVIATION 2"))
fig1.add_trace(go.Scatter(x=[weight_second_std_dev_end, weight_second_std_dev_end], y=[0, 0.005], mode="lines", name="STANDARD DEVIATION 2"))
fig1.show()