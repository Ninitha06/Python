import plotly.express as px
import csv
import numpy as np

# with open("./csv/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv",newline='') as f:
#     df = csv.DictReader(f)
#     fig = px.scatter(df,x="Temperature",y="Ice-cream Sales")

#     fig.show()


# with open("./csv/cups of coffee vs hours of sleep.csv",newline='') as g:
#     df1=csv.DictReader(g)
#     fig1 = px.scatter(df1,x="Coffee in ml",y="sleep in hours")

#     fig1.show()


def getDataSource(data_path):
    temp=[]
    colddrink=[]
    with open(data_path,newline='') as h:
        df2=csv.DictReader(h)
        for row in df2:
            print(row) 
            temp.append(float(row["Temperature"]))
            colddrink.append(float(row["Cold drink sales"]))
    return {"x":temp,"y":colddrink}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("Correlation is " + str(correlation[0,1]))


def main():
    dataSource = getDataSource("./csv/Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv")
    findCorrelation(dataSource)


main()