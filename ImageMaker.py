
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os
import textwrap

def splitStr(text):
    block=""
    size=65
    strlist=[]
    count=0
    for ch in text:
       # print(ch)
        block=block+ch
        count=count+1
        if(count==size):
            strlist.append(block)
            block=""
            count=0
    strlist.append(block)       
    k=3-len(strlist)   
    v=0
    while(v<k):
        strlist.append("")
        v=v+1
    
    return strlist  

def isImageCreated(farmername,farmermobile,yield_result,suggestion_result,predicted_price,n,p,k,ph,crop,temp,hum,rain,villagename,sod):
    flag=0
    img = Image.open('model/sample1.jpg')
    suggestion=suggestion_result
    print("Suggestion length ",len(suggestion))
    strlist=splitStr(suggestion)
   # sug=textwrap.wrap(suggestion, 60)
    
    sug1=strlist[0]
    sug2=strlist[1]
    sug3=strlist[2]
    
    print("sug1 ",sug1)
    print("sug2 ",sug2)
    print("sug3 ",sug3)
    
    
    image_filename="reports//"+farmername+"_"+farmermobile+".jpg"
    
      
    finaltext1="FARMER NAME :" + farmername
    finaltext2="MOBILE NUMBER : "+farmermobile
    finaltext3="CROP : "+crop
    finaltext31="VILLAGE : "+villagename
    finaltext32="SOWING DATE : "+sod
    
    finaltext4="TEMPERATURE : "+str(temp)+" Celsius"
    finaltext5="HUMIDITY : "+str(hum)+" (g/kg)"
    finaltext6="RAINFALL : "+str(rain)+" mm"
    finaltext7="NITROGEN (N) : "+n+" Kg /ha"
    finaltext8="PHOSPHORUS (P) : "+p+" Kg /ha"
    finaltext9="POTTASIUM (K) : "+k+" Kg /ha"
    finaltext10="Ph : "+ph
    finaltext11=yield_result
    finaltext12="PREDICTED PRICE : "+predicted_price+" Rs Per Quintal"
    finaltext13="SUGGESTION RESULT BELOW :"
    finaltext14=sug1
    finaltext15=sug2
    finaltext16=sug3
    
    finaltext17="Thanks and Regards"
    finaltext18="CROP YIELD AND PRICE PREDICTION SYSTEM."
   
        
    # Call draw Method to add 2D graphics in an image
    I1 = ImageDraw.Draw(img)
     
    # Custom font style and font size
    myFont = ImageFont.truetype('arial.ttf', 40)
    newfont = ImageFont.truetype('arial.ttf', 40)
    #myFont = ImageFont.load_default()
     
    # Add Text to an image
    I1.text((80, 350), finaltext1, font=myFont, fill =(0, 0, 0))
    I1.text((80, 450), finaltext2, font=myFont, fill =(0, 0, 0))
    I1.text((80, 550), finaltext3, font=myFont, fill =(0, 0, 0))
    I1.text((80, 650), finaltext31, font=myFont, fill =(0, 0, 0))
    I1.text((80, 750), finaltext32, font=myFont, fill =(0, 0, 0))
    
    I1.text((80, 850), finaltext4, font=myFont, fill =(0, 0, 0))
    I1.text((80, 950), finaltext5, font=myFont, fill =(0, 0, 0))
    
    I1.text((80, 1050), finaltext6, font=myFont, fill =(0, 0, 0))
    I1.text((80, 1150), finaltext7, font=myFont, fill =(0, 0, 0))
    I1.text((80, 1250), finaltext8, font=myFont, fill =(0, 0, 0))
    I1.text((80, 1350), finaltext9, font=myFont, fill =(0, 0, 0))
    I1.text((80, 1450), finaltext10, font=myFont, fill =(0, 0, 0))
 
    I1.text((80, 1550), finaltext11, font=myFont, fill =(0, 0, 0))
    I1.text((80, 1650), finaltext12, font=myFont, fill =(0, 0, 0))
    I1.text((80, 1750), finaltext13, font=myFont, fill =(200, 0, 0))
    I1.text((80, 1850), finaltext14, font=newfont, fill =(0, 0, 128))
    I1.text((80, 1950), finaltext15, font=newfont, fill =(0, 0, 128))
    I1.text((80, 2050), finaltext16, font=newfont, fill =(0, 0, 128))
    
    I1.text((80, 2550), finaltext17, font=myFont, fill =(255, 0, 0))
    I1.text((80, 2350), finaltext18, font=myFont, fill =(0, 0, 255))
    
    

    
    img.save(image_filename)    
        
     


    
    flag=1
            
        
    
    return flag
   

    
