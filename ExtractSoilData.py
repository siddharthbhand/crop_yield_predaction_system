from pymata4 import pymata4
import time 


def getSoilParameters():
    
    moisture_reading=0   
    board = pymata4.Pymata4(com_port="COM5")  # Specify COM5 as the port
    
    analog_pin = 0
    digital_pin = 8
    
    board.set_pin_mode_analog_input(analog_pin)
    board.set_pin_mode_digital_input(digital_pin)
    count=0
    
    while True:
        value, _ = board.analog_read(analog_pin)  # Read analog value and ignore timestamp
        if value is not None:
            moisture_reading=value
            print(moisture_reading)
            count=count+1
            if(count==10):
                break
            
        
           
        time.sleep(1)
    
    
    
   
    npk_conversion_factor = 0.2
    nitrogen_factor = 0.5
    phosphorus_factor = 0.3
    potassium_factor = 0.2
    
    # Convert moisture reading to NPK values
    npk_value = moisture_reading * npk_conversion_factor
    nitrogen = int(npk_value * nitrogen_factor)
    phosphorus = int(npk_value * phosphorus_factor)
    potassium = int(npk_value * potassium_factor)
    
    ph_conversion_factor = 0.01
    
    # Convert moisture reading to pH value
    ph_value = (moisture_reading/2) * ph_conversion_factor
    return nitrogen,phosphorus,potassium,ph_value