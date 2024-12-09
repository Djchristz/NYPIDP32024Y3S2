# import spidev as adc
import RPi.GPIO as GPIO
import time

##########################################
# Whack all the GPIO Pins here, lazy anyhow define
#Motor 1, Remember change pin. Unchanged as of 19/11/2024
fmotor1 = 17  # Forward
rmotor1 = 27  # GoStan 
spmotor1 = 22  # Speed pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(fmotor1, GPIO.OUT)
GPIO.setup(rmotor1, GPIO.OUT)
GPIO.setup(spmotor1, GPIO.OUT)

pwm = GPIO.PWN(spmotor1, 1000)
pwm.start(90) #Speed
#Motor 2
fmotor2 = 17  # Forward
rmotor2 = 27  # GoStan 
spmotor2 = 22  # Speed pin

GPIO.setup(fmotor2, GPIO.OUT)
GPIO.setup(rmotor2, GPIO.OUT)
GPIO.setup(spmotor2, GPIO.OUT)

pwm = GPIO.PWN(spmotor2, 1000)
pwm.start(90) #Speed
#Motor 3
fmotor3 = 17  # Forward
rmotor3 = 27  # GoStan 
spmotor3 = 22  # Speed pin

GPIO.setup(fmotor3, GPIO.OUT)
GPIO.setup(rmotor3, GPIO.OUT)
GPIO.setup(spmotor3, GPIO.OUT)

pwm = GPIO.PWN(spmotor3, 1000)
pwm.start(90) #Speed

ultrasonic_trigger = 1 #Pins
ultrasonic_echo = 2

GPIO.setup(ultrasonic_trigger, GPIO.OUT)
GPIO.setup(ultrasonic_echo, GPIO.IN)

irsens = read_adc(0)
irreadings = []

state = 1  # Starting state
last_hand_detected = False  
scan_rejected = False  
scan_accepted = False


# ADC setup (example for MCP3008 on SPI interface)
# adc = adc.SpiDev()
# adc.open(0, 0)  # Open on bus 0, device 0
# adc.max_speed_hz = 1350000

#IR Reading 
def read_adc(channel):  # MCP3008 ADC Protocol
    irreading = adc.xfer2([1, (8 + channel) << 4, 0])
    data = ((irreading[1] & 3) << 8) + irreading[2]
    return data

def irscanning():
    m1f(0.1)
    irreadings.append(irsens)

    if len(irreadings) > 2:
        # Trim the first and last readings
        trimmed_readings = irreadings[1:-1]

        contaminated = False
        # Check for contamination in the trimmed readings
        for i in range(1, len(trimmed_readings) - 1):
            if abs(trimmed_readings[i] - trimmed_readings[i-1]) > 100 or abs(trimmed_readings[i] - trimmed_readings[i+1]) > 100:
                contaminated = True
                break

        # Handle contamination or acceptance
        if contaminated:
            scan_rejected = True
            print("Contamination detected. Recyclable rejected.")
        else:
            scan_rejected = False
            print("No contamination. Recyclable accepted.")
        print("Processed readings (after trimming):", trimmed_readings)
        return scan_rejected
    else:
        print("Not enough data to process.")
    time.sleep(0.1)
#IR Reading End

#Motor Controls
#M1 Conveyor, M2 Door, M3 Nothing for now
def m1f(timestop): #Forward
    GPIO.output(fmotor1, GPIO.HIGH)
    GPIO.output(rmotor1, GPIO.LOW)
    time.sleep(timestop)
    m1s()

def m1r(timestop): #Reverse
    GPIO.output(fmotor1, GPIO.LOW)
    GPIO.output(rmotor1, GPIO.HIGH)
    time.sleep(timestop)
    m1s()

def m1s(): #Stop
    GPIO.output(fmotor1, GPIO.LOW)
    GPIO.output(rmotor1, GPIO.LOW)

def m2f(timestop):
    GPIO.output(fmotor2, GPIO.HIGH)
    GPIO.output(rmotor2, GPIO.LOW)
    time.sleep(timestop)
    m2s()

def m2r(timestop):
    GPIO.output(fmotor2, GPIO.LOW)
    GPIO.output(rmotor2, GPIO.HIGH)
    time.sleep(timestop)
    m2s()

def m2s():
    GPIO.output(fmotor2, GPIO.LOW)
    GPIO.output(rmotor2, GPIO.LOW)

def m3f(timestop):
    GPIO.output(fmotor3, GPIO.HIGH)
    GPIO.output(rmotor3, GPIO.LOW)
    time.sleep(timestop)

def m3r(timestop):
    GPIO.output(fmotor3, GPIO.LOW)
    GPIO.output(rmotor3, GPIO.HIGH)
    time.sleep(timestop)

def m3s():
    GPIO.output(fmotor3, GPIO.LOW)
    GPIO.output(rmotor3, GPIO.LOW)
#Motor Controls end

#Conveyor Logic
def conveyor():
    m1f(2)
    #Rainier AI scan 
    #Another need to wait for Rainier part
    irscanning()
    if irscanning():
        state = 4
    else:
        state = 1

#Conveyor Logic End

#ultrasonic logic
def ultrasonicbutton():
    # Send a 10us pulse to the trigger
    GPIO.output(ultrasonic_trigger, GPIO.LOW)
    time.sleep(0.1)  # Delay to stabilize
    GPIO.output(ultrasonic_trigger, GPIO.HIGH)
    time.sleep(0.00001)  # 10 microseconds pulse
    GPIO.output(ultrasonic_trigger, GPIO.LOW)

    # Measure the time for the echo to return
    while GPIO.input(ultrasonic_echo) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ultrasonic_echo) == GPIO.HIGH:
        pulse_end = time.time()

    # Calculate distance (speed of sound is ~34300 cm/s)
    pulse_duration = pulse_end - pulse_start
    distance = (pulse_duration * 34300) / 2  # Divide by 2 for round trip
    return distance

#ultrasonic logic end

