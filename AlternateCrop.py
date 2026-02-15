import csv
import operator
import collections
def getAlternateCropName(n,p,k,ph,temp,hum,rain,crop):
    
    print("INSIDE THE ALTERNATER CROP")
    n_min=int(n)-5
    n_max=int(n)+5
    
    p_min=int(p)-5
    p_max=int(p)+5
    
    k_min=int(k)-5
    k_max=int(k)+5
    
    ph_min=float(ph)-2
    ph_max=float(ph)+2
    
    temp_min=float(temp)-4
    temp_max=float(temp)+4

    hum_min=float(hum)-10
    hum_max=float(hum)+10
    
    rain_min=float(rain)-25
    rain_max=float(rain)+25
    csv_file_path = 'model/prediction_results.csv'
    pred_data_list = []
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            pred_data_list.append(row)
            
    datasetpath='model/crop_yield_dataset.csv'
    dataset_list = []
    with open(datasetpath, 'r') as file:
        csv_reader = csv.reader(file)
        
        for row in csv_reader:
            dataset_list.append(row)        
    predicted_Selected__list=[]        
    for row in pred_data_list:
        rn=row[0]
        rownumber=int(rn)
        rowdata=dataset_list[rownumber]
        predicted_Selected__list.append(rowdata)
    count=0 
    sel_crop_list=[]
    for row in predicted_Selected__list:
        DN=int(row[0])
        DP=int(row[1])
        DK=int(row[2])
        DPH=float(row[5])
        DTMP=float(row[3])
        DHUM=float(row[4])
        DRAIN=float(row[6])
        CROP=row[7]
        if(DN>=n_min and DN<=n_max):
            count=count+1
        if(DP>=p_min and DP<=p_max):
            count=count+1
            
        if(DK>=k_min and DK<=k_max):
            count=count+1
        if(DPH>=ph_min and DPH<=ph_max):
            count=count+1
        if(DTMP>=temp_min and DTMP<=temp_max):
            count=count+1
        if(DHUM>=hum_min and DHUM<=hum_max):
            count=count+1    
        if(DRAIN>=rain_min and DRAIN<=rain_max):
            count=count+1        
        if(count>=6):
            sel_crop_list.append(CROP)
   # print("alternate CROP ===",sel_crop_list) 
    altcropnames=""
    if(len(sel_crop_list)>0):
        frequency = collections.Counter(sel_crop_list)
        cropfreq=dict(frequency)
        sorted_d = sorted(cropfreq.items(), key=operator.itemgetter(1))
        print('Dictionary in ascending order by value : ',sorted_d)
        size=len(sorted_d)-1
        
        fincount=0
       
        for i in reversed(range(size + 1)) :
            temprow=sorted_d[i]
            altcrp=temprow[0]
            if(altcrp!=crop):
                altcropnames=altcropnames+" , "+altcrp
                fincount=fincount+1
                if(fincount==3):
                    break
    
    print("Alternate crops are : ", altcropnames)        
    return  altcropnames        
         