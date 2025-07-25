import machine
import time

# Configuration
adc_pin = 34
relay_pin = 15
moisture_threshold = 30.0  # Percentage threshold to turn pump ON

# Setup ADC
adc = machine.ADC(machine.Pin(adc_pin))
adc.atten(machine.ADC.ATTN_11DB)  # 0-3.6V range
adc.width(machine.ADC.WIDTH_12BIT)  # 0-4095

# Setup relay pin as output
relay = machine.Pin(relay_pin, machine.Pin.OUT)
relay.value(0)  # Start with pump OFF (adjust if needed)

def read_moisture():
    raw = adc.read()
    percent = 100 - (raw / 4095 * 100)  # invert if sensor logic requires
    return raw, percent

def log_reading(raw, percent, pump_status):
    timestamp = time.time()
    with open("moisture_log.txt", "a") as f:
        f.write("{},{:.2f},{}\n".format(timestamp, percent, pump_status))

while True:
    raw, moisture = read_moisture()
    pump_on = False

    if moisture < moisture_threshold:
        relay.value(1)  # Turn pump ON
        pump_on = True
    else:
        relay.value(0)  # Turn pump OFF

    status = "ON" if pump_on else "OFF"
    print("Moisture: {:.2f}% | Pump: {}".format(moisture, status))
    log_reading(raw, moisture, status)

    time.sleep(10)  # wait 10 seconds before next reading
