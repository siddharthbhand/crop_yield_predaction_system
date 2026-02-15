import pywhatkit as pwk
import datetime


def sendInfoWA(newfilename,number,message):
   
    mobilenumber="+91"+number;
 
    reference_image_path=newfilename
    
   # WhatsAppSender.sendImage(mobilenumber, reference_image_path, message)
    print("File path is ",newfilename)
    datet=str(datetime.datetime.now())
    st=datet.split(" ")
    kt=st[1].split(":")
    hourstr=kt[0]
    minstr=kt[1]
    hr=int(hourstr)
    min=int(minstr)
    if(min<59):
        min=min+1
    else:
        min=1
        hr=hr+1
    print(hr)
    print(min)
    
   
    pwk.sendwhats_image(mobilenumber, reference_image_path,message)
    
 
if __name__ == '__main__':
    sendInfoWA()
 