import pandas as pd
import random

def getWeatherParameters(villagename):
        
    datasetpath = 'model/static_weather_dataset.xlsx'
    df = pd.read_excel(datasetpath, sheet_name='weather')
    data=df.values.tolist()
   # print(data)
    selected_weather_data = []
   
       
    for row in data:
        selectedvillage=row[3]
        if(selectedvillage==villagename):
            temp=[]
            temp.append(row[0])
            temp.append(row[1])
            temp.append(row[2])
            
            selected_weather_data.append(temp)
           # print(temp)
    n=len(selected_weather_data)
    print("Number of Weather parameter for the selected Village : ",n)
    index= random. randint(0,n)
    print("index = ",index)
    newrow=selected_weather_data[index]
    temperature=newrow[0]
    humidity=newrow[1]
    rainfall=newrow[2]
    return temperature,humidity,rainfall
    
   
    


# temperature,humidity,rainfall=getWeatherParameters("Sangamner")        
# print("temperature : ",temperature)
# print("humidity : ",humidity)
# print("rainfall : ",rainfall)

        

        