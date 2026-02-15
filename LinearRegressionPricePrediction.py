import pandas as pd

def getPricePrediction(cropname,rainfall):
        
    datasetpath = 'model/AgrcultureDataset_Maharashtra_2.0.xlsx'
    df = pd.read_excel(datasetpath, sheet_name='Sheet2')
    data=df.values.tolist()
   # print(data)
    selected_data = []
   
       
    for row in data:
        selectedcrop=row[3]
        if(selectedcrop==cropname):
            temp=[]
            temp.append(row[4])
            temp.append(row[5])
            selected_data.append(temp)
            print(temp)
    
    
    
    sumx,sumy,sumxy,sumx2=0.0,0.0,0.0,0.0
    N=len(selected_data)
    for row in selected_data:
        rainstr=row[0]
        pricestr=row[1]
        x=float(rainstr)
        y=float(pricestr)
        sumx=sumx+x
        sumy=sumy+y
        sumxy=sumxy+(x*y)
        sumx2=sumx2+(x*x)
       # sumy2=symy2=(y*y)
    nr=N*sumxy-sumx*sumy
    dr=N*sumx2-(sumx*sumx)
    m_slope=nr/dr
    print("m_slope ",m_slope)
    
    b_intercept=(sumy-m_slope*sumx)/N
    print("b_intercept ",b_intercept)
    rainf=float(rainfall)
    predicted_price=m_slope*rainf+b_intercept
    predicted_price=round(predicted_price,2)
   
    return str(predicted_price)
    



# cropname="cotton"
# rainfall="150.23"
        
# getPricePrediction(cropname,rainfall)        
        

        