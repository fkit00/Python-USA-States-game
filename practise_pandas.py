#with open("weather_data.csv") as data_file:
  #  data = data_file.readlines() ## takes each line and turns it into a list item
    #print(data)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps=[]
#     for row in data: 
#         if row[1] != "temp":
        
#             temps.append(int(row[1]))
#     print(temps)

import pandas

data = pandas.read_csv('weather_data.csv')
#print(data['temp'])

# data_dict= data.to_dict()
# print(data_dict)

# temp_list=data["temp"].to_list()
# print(temp_list)

#average_temp = sum(temp_list)/len(temp_list)
#print(average_temp)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.condition) 
# finding the row with the highest temp

#print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp*9/5+32
# print(monday_temp_f)

#create a dataframe from scratch

