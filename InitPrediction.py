import CropYieldEstimator
import LinearRegressionPricePrediction
import ImageMaker

import samwa
def startPrediction(farmername,farmermobile,n, p, k,ph, temp, hum,  rain, crop,villagename,sod):
    yield_result,suggestion_result="",""
    yield_result,suggestion_result=CropYieldEstimator.getCropPredictionParameter(n,p,k,temp,hum,ph,rain,crop)
    
   
        
    print("yield_result : ",yield_result)
    print("suggestion_result : ",suggestion_result)
    
    predicted_price=LinearRegressionPricePrediction.getPricePrediction(crop, rain)
    
    print("Predicted Price : ",predicted_price)
    flag=ImageMaker.isImageCreated(farmername, farmermobile, yield_result, suggestion_result, predicted_price, n, p, k, ph, crop, temp, hum, rain,villagename,sod)
    if(flag==1):
        print("Created wwwwwwwwwwwww")
        image_filename="reports/"+farmername+"_"+farmermobile+".jpg"
               
        
        message="Dear Farmer " +farmername 
        message=message+"\n Please find the Prediction analysis Report for the entered crop\n"
        message=message+"\nThanks and Regards\n Automatic Crop Price and Yield prediction System"
        message=message+"\n"+"*** HAPPY FARMING ***"
        samwa.sendInfoWA(image_filename, farmermobile, message)
       # WhatsAppSender.sendInfoWA(image_filename, message, farmermobile)
     
    
        
    
    













# farmername="kiran"
# farmermobile="9284604268"
# n='90'
# p='42'
# k='20'
# temp='20.98'
# hum='72.68'
# ph='6.561'
# rain='100.00'
# crop='apple'
# startPrediction(farmername,farmermobile,n, p, k,ph, temp, hum,  rain, crop)
