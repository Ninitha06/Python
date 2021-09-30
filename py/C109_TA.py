import random
import statistics

import plotly.figure_factory as ff

dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)


mean_data = sum(dice_result)/len(dice_result)
std_dev = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

print(mean_data)
print(std_dev)
print(median)
print(mode)

fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()