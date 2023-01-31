import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(gray)
print(cinnamon)
print(black)

data_dict={
    "Fur colour":["Gray", "Cinnamon","Black"], 
    "Count":[gray,cinnamon,black]
}

data_frame=pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel_count.csv")