import numpy as np
import csv
import plotly_express as px




def getDataSource():
    data1 = []
    data2 = []

    # with open('./csv/Size of TV,_Average time spent watching TV in a week (hours).csv',newline='') as f:
    #     df = csv.DictReader(f)
    # #  file objects in python are generators, so you have to reopen the file to loop more than once. –
    #     # fig = px.scatter(df,x='Size of TV',y='\tAverage time spent watching TV in a week (hours)')
    #     # fig.show()
        
    #     for row in df:
    #         print(row)
    #         data1.append(float(row["Size of TV"]))
           
    #         data2.append(float(row[' Average time spent watching TV in a week (hours)']))
           
    # return {"x" : data1,"y" : data2}
    with open('./csv/Student Marks vs Days Present.csv',newline='') as f:
        df = csv.DictReader(f)
    #  file objects in python are generators, so you have to reopen the file to loop more than once. –
        # fig = px.scatter(df,x='Size of TV',y='\tAverage time spent watching TV in a week (hours)')
        # fig.show()
        
        for row in df:
            data1.append(float(row["Marks In Percentage"]))
           
            data2.append(float(row['Days Present']))
           
    return {"x" : data1,"y" : data2}

def getCorrelation(dataSource) :
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation is " +str (correlation[0,1]))

ds = getDataSource()
getCorrelation(ds)