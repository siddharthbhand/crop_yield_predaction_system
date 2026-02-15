def convert_moisture_to_ph(moisture_reading):
    # Define some arbitrary conversion factors
    # These factors would need to be calibrated based on your specific soil and sensor characteristics
    ph_conversion_factor = 0.01
    
    # Convert moisture reading to pH value
    ph_value = (moisture_reading/2) * ph_conversion_factor
    
    return ph_value


def convert_moisture_to_npk(moisture_reading):
    # Define some arbitrary conversion factors
    # These factors would need to be calibrated based on your specific soil and sensor characteristics
    npk_conversion_factor = 0.2
    nitrogen_factor = 0.5
    phosphorus_factor = 0.3
    potassium_factor = 0.2
    
    # Convert moisture reading to NPK values
    npk_value = moisture_reading * npk_conversion_factor
    nitrogen = int(npk_value * nitrogen_factor)
    phosphorus = int(npk_value * phosphorus_factor)
    potassium = int(npk_value * potassium_factor)
    
    
    return nitrogen, phosphorus, potassium

# Example moisture reading
moisture_reading = 1023  # Example reading from soil moisture sensor

# Convert moisture reading to NPK values
nitrogen, phosphorus, potassium = convert_moisture_to_npk(moisture_reading)

print("Nitrogen (N):", nitrogen)
print("Phosphorus(P) :", phosphorus)
print("Potassium (K):", potassium)

ph = convert_moisture_to_ph(moisture_reading)

print("pH value:", ph)