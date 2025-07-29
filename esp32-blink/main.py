from machine import Pin, ADC
import time


moisture_sensor_pin = ADC(Pin(34))


moisture_sensor_pin.atten(ADC.ATTN_11DB)

#
DRY_CALIBRATION_VALUE = 3700 # Example: Value when sensor is in air/very dry
WET_CALIBRATION_VALUE = 900  # Example: Value when sensor is in water/very wet
# --------------------------------------------------

print("Soil Moisture Sensor Calibration & Test")
print("---------------------------------------")
print(f"Dry Reference Value (higher ADC value): {DRY_CALIBRATION_VALUE}")
print(f"Wet Reference Value (lower ADC value): {WET_CALIBRATION_VALUE}")
print("---------------------------------------")

def map_range(value, in_min, in_max, out_min, out_max):
    """
    Re-maps a number from one range to another.
    Similar to Arduino's map() function.
    """
    return (value - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

while True:
    moisture_raw = moisture_sensor_pin.read() 

    
    moisture_percent = map_range(moisture_raw, DRY_CALIBRATION_VALUE, WET_CALIBRATION_VALUE, 0, 100)
    
    # Constrain the percentage to be within 0-100
    if moisture_percent < 0:
        moisture_percent = 0
    elif moisture_percent > 100:
        moisture_percent = 100

    print(f"Raw: {moisture_raw} | Moisture (%): {moisture_percent}")

    
    if moisture_percent < 30: 
        print("--> Soil is DRY! Needs water.")
        
    elif moisture_percent > 70: 
        print("--> Soil is WET! No need for water.")
    else:
        print("--> Soil is Moist. All good.")

    time.sleep(2) 