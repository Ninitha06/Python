import csv
from collections import Counter

with open("./csv/HeightWeight.csv",newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

# print(file_data)
file_data.pop(0)
# print(file_data)

#Sorting data to get height
new_data = []
for i in range(len(file_data)) :
    n_num = file_data[i][1]
    new_data.append(float(n_num))


#calculate mean

n = len(new_data)
total = 0
for x in new_data:
    total = total + x

mean = total/n

print("Mean is " + str(mean))

#Calculate Mode
new_data.sort()

if(n%2==0):
    #n/2 gives 12500.0 which throws error to have in array indices.
    #print("Hi " + str(n/2))
    median1 = float(new_data[n//2])
    median2 = float(new_data[n//2-1])
    median = (median1+median2)/2
else :
    median = float(new_data[n//2])

print("Median " + str(median))

#calculating Mode

data = Counter(new_data)
#cant have curly braces on new line
mode_data_range = {
    "50-60" : 0,
    "60-70" : 0,
    "70-80" : 0,
}

for height,occurence in data.items():
    if 50<float(height)<60:
        mode_data_range["50-60"]=mode_data_range["50-60"]+occurence
    elif 60<float(height)<70:
        mode_data_range["60-70"]=mode_data_range["60-70"]+occurence
    elif 70<float(height)<80:
        mode_data_range["70-80"]=mode_data_range["70-80"]+occurence

print(mode_data_range)

mode_range,mode_occurence = 0,0

for range,occurence in mode_data_range.items():
    if(occurence>mode_occurence):
        mode_range,mode_occurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence
mode = float(mode_range[0] + mode_range[1])/2

#print(f"Mode  {mode}") - it works

# :2f is equivalent to %2f - : is called formatting symbols. f in the beginning is the short form for format
print(f"Mode {mode:2f}")

# from collections import Counter

# new_data = "whitehatjr"
# data = Counter(new_data)
# print(data)
# new_list = data.items()
# print(new_list)

# value = data.values()
# print(value)