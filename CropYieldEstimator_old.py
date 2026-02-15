import csv

def getCropPredictionParameter(n,p,k,temp,hum,ph,rainfall,crop):
        
    csv_file_path = 'model/prediction_results.csv'
    pred_data_list = []
    predicted_fetched_list=[]
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
    
        for row in csv_reader:
            pred_data_list.append(row)
   
            
    for row in pred_data_list:
        selectedcrop=row[1]
        if(selectedcrop==crop):
            predicted_fetched_list.append(row)
            print(row)
            
            
            
     
   
    datasetpath='model/crop_yield_dataset.csv'
    dataset_list = []
    with open(datasetpath, 'r') as file:
        csv_reader = csv.reader(file)
       
        for row in csv_reader:
            dataset_list.append(row)
            
   
    predicted_Selected__list=[]
    pred_N_list=[]
    pred_P_list=[]
    pred_K_list=[]
    pred_temp_list=[]
    pred_hum_list=[]
    pred_ph_list=[]
    pred_rain_list=[]
    
    for row in predicted_fetched_list:
        rn=row[0]
        rownumber=int(rn)
        rowdata=dataset_list[rownumber]
        predicted_Selected__list.append(rowdata)
        pred_N_list.append(rowdata[0])
        pred_P_list.append(rowdata[1])
        pred_K_list.append(rowdata[2])
        pred_temp_list.append(rowdata[3])
        pred_hum_list.append(rowdata[4])
        pred_ph_list.append(rowdata[5])
        pred_rain_list.append(rowdata[6])
        
        print(rowdata)
        
        
    
    print(pred_rain_list)
            
    min_n_1=min(pred_N_list)
    max_n_2=max(pred_N_list)
    min_n_va=float(min_n_1)
    max_n_va=float(max_n_2)
    
    
    min_p_1=min(pred_P_list)
    max_p_2=max(pred_P_list)
    min_p_va=float(min_p_1)
    max_p_va=float(max_p_2)
    
    
    min_k_1=min(pred_K_list)
    max_k_2=max(pred_K_list)
    min_k_va=float(min_k_1)
    max_k_va=float(max_k_2)
    
    
    
    min_temp=min(pred_temp_list)
    max_temp=max(pred_temp_list)
    min_temp_va=float(min_temp)
    max_temp_va=float(max_temp)
    
    
    min_hum=min(pred_hum_list)
    max_hum=max(pred_hum_list)
    min_hum_va=float(min_hum)
    max_hum_va=float(max_hum)
    
    min_ph=min(pred_ph_list)
    max_ph=max(pred_ph_list)
    min_ph_va=float(min_ph)
    max_ph_va=float(max_ph)
    
    
    min_rain=min(pred_rain_list)
    max_rain=max(pred_rain_list)
    
    min_rain_va=float(min_rain)
    max_rain_va=float(max_rain)
    
    print("min_n_va : ",min_n_va)
    print("max_n_va : ",max_n_va)
    
    print("min_p_va : ",min_p_va)
    print("max_p_va : ",max_p_va)
    
    print("min_k_va : ",min_k_va)
    print("max_k_va : ",max_k_va)
    
    print("min_temp_va : ",min_temp_va)
    print("max_temp_va : ",max_temp_va)
    
    print("min_hum_va : ",min_hum_va)
    print("max_hum_va : ",max_hum_va)
    
    print("min_ph_va : ",min_ph_va)
    print("max_ph_va : ",max_ph_va)
        
    print("min_rain_va : ",min_rain_va)
    print("max_rain_va : ",max_rain_va)
    
   
    N=float(n)
    P=float(p)
    K=float(k)
    TEMP=float(temp)
    HUM=float(hum)
    PH=float(ph)
    RAIN=float(rainfall)
    
    
    
    
    
    parametercount=0;
    ncount=0
    pcount=0
    kcount=0
    phcount=0
    ferticount=0
    deficiency=[]
    
    
    if(N>=min_n_va and N<=max_n_va):
        parametercount=parametercount+1
        ferticount=ferticount+1
    else:
        deficiency.append("NITRONGEN")
        
    if(P>=min_p_va and P<=max_p_va):
        parametercount=parametercount+1
        ferticount=ferticount+1
    else:
         deficiency.append("PHOSPHORUS")   
    
    if(K>=min_k_va and K<=max_k_va):
        parametercount=parametercount+1
        ferticount=ferticount+1
    else:
        deficiency.append("POTTASSIUM")  
    
    if(PH>=min_ph_va and PH<=max_ph_va):
        parametercount=parametercount+1  
        ferticount=ferticount+1   
    else:
        deficiency.append("PH IMBALANCE") 
    
    if(TEMP>=min_temp_va and TEMP<=max_temp_va):
        parametercount=parametercount+1   
                 
    if(HUM>=min_hum_va and HUM<=max_hum_va):
        parametercount=parametercount+1   
             
    if(RAIN>=min_rain_va and RAIN<=max_rain_va):
        parametercount=parametercount+1     
              
    print("N : ",n)
    print("P : ",p)
    print("K : ",k)
    print("TEMP : ",temp)
    print("HUM: ",hum)
    print("PH: ",ph)
    print("RAINFALL :",rainfall)
    print("CROP : ",crop)    
    print("parametercount = ",parametercount)
    print("ferticount = ",ferticount)
    
    
    suggestion_result=""
    
    print("deficiency : ",deficiency)
    defstr=""
    for text in deficiency:
        defstr=defstr+" "+text+" , "
        
    import AlternateCrop
    altcrop=AlternateCrop.getAlternateCropName(n, p, k, ph, temp, hum, rainfall,crop)  
    
    yieldresultdict=["WORST With 05% Yeild","VERY VERY LOW: With 15% Yeild","VERY LOW: With 25% Yeild","LOW: With 30% Yield","BELOW AVERAGE: With 40% Yield","AVERAGE: With 60% Yield","HIGH: With 75% Yield","VERY HIGH: With 85% Yield","VERY VERY HIGH: With 100% Yeild"]
    suggestiondict=["WORST CONDITION,STOP ALL ACTIVITIES AND  PLEASE CONSULT AGRICULTURE OFFICEER","DO NOT GO FOR THIS CROP AT ANY COST"," DO NOT SOW THIS CROP, GO FOR  OTHER CROP"," AS THE YIELD IS LOW, GO FOR OTHER CROP"]
    if(parametercount<=3):
        suggestion_result=suggestiondict[parametercount]+" SOIL IS HAVING DEFICIENCY OF "+defstr+" AND ALTERNATE CROPS ARE "+altcrop
        
    elif(ferticount<4 and parametercount==4):
        suggestion_result=" PLEASE DO THOROUGH SOIL TESTING AND ALSO WEATHER IS NOT GOOD TO SOW NOW"+" AND SOIL IS HAVING DEFICIENCY OF "+defstr+" AND ALTERNATE CROPS ARE "+altcrop
    
    elif(ferticount<4 and parametercount==5):
         suggestion_result="WEATHER IS AVERAGE  TO GET GOOD YIELD, GO WITH YOUR INSTINCT "+" AND SOIL IS HAVING DEFICIENCY OF "+defstr+" AND ALTERNATE CROPS ARE "+altcrop
         
         
    elif(parametercount==5):
        suggestion_result="WEATHER IS AVERAGE  TO GET GOOD YIELD, GO WITH YOUR INSTINCT "                                                     
      
    elif(ferticount<4 and parametercount==6):    
        suggestion_result=" USE BETTER FERTILIZERS TO GET EVEN MORE YIELD "+" AND SOIL IS HAVING DEFICIENCY OF "+defstr
        
    elif(parametercount==6):    
        suggestion_result=" GOOD ENOUGH PARAMETERS,ALSO CONSULT AGRI EXPERT ONCE "
        
        
    elif( parametercount==7):    
        suggestion_result=" EVERYTHING IS GOOD, GO FOR IT, BEST OF LUCK"
   
    
        
        
    
   
    yieldresultstr=yieldresultdict[parametercount]
    yield_result=" CROP YIELD RESULT : "+yieldresultstr
    suggestion_result_fin=suggestion_result
    print("yield_result : ",yield_result)
    print("suggestion_result_fin : ",suggestion_result_fin)
    
    
    return yield_result,suggestion_result_fin

# n=98
# p=75
# k=41
# ph=5.2
# temp=30.69
# hum=85.89

# rainfall=140
# crop="rice"

        
# getCropPredictionParameter(n,p,k,temp,hum,ph,rainfall,crop)    
       
        