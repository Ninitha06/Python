import math
import csv

#Read the contents from csv file.
with open("./csv/data_sd.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# file_data is array in an array when using data.csv. Master/main array has only 1 element which is the actual data array.
print(file_data)
# if using class1.csv kinda data.
#     file_data.pop(0)

# data = []
# for x in file_data:
#     data.append(x[1])
    
data = file_data[0]
print(data)

#Function for mean of data
def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total = total + int(x)
    
    mean = total/n
    return mean

#store the mean in a variable
mean_data = mean(data)

#Get the square of difference btw numbers and mean
square_list = []
for num in data :
    a = int(num)-mean_data
    a=a**2
    square_list.append(a)

#get the sum of the above.
sum=0
for i in square_list:
    sum = sum + i


result = sum/(len(data)-1)

std_deviation = math.sqrt(result)
print("Standard Deviation : " + str(std_deviation))
