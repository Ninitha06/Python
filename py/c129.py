import csv

# https://exoplanetarchive.ipac.caltech.edu/docs/table-redirect.html

#  Composite parameters table in the above website
data = []

with open("tabledata.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

# REmove the meta data at the top manually after downloading from website.
headers = data[0]
planet_data = data[1:]

#Converting all planet names to lower case
for data_point in planet_data:
    # recent csv has planet names in 1st column
    # print(data_point[0])
    data_point[0] = data_point[0].lower()

#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[0])


with open("tabledata_sorted.csv", "a+",newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)


data = []

with open("scraping_final.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

# REmove the meta data at the top manually after downloading from website.
headers = data[0]
planet_data = data[1:]

#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[0])


with open("scraping_final_sorted.csv", "a+",newline='') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)