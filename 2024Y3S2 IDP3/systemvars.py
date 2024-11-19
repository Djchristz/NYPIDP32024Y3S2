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

# ultrasonic_trigger = 1 ## thats if we even have ultrasonic sensor
# ultrasonic_echo = 2

# GPIO.setup(ultrasonic_trigger, GPIO.OUT)
# GPIO.setup(ultrasonic_echo, GPIO.IN)
#########################################

irsens = read_adc(0)


# ADC setup (example for MCP3008 on SPI interface)
# adc = adc.SpiDev()
# adc.open(0, 0)  # Open on bus 0, device 0
# adc.max_speed_hz = 1350000

global scan_mat_type
global scan_mat

# plastics_data = {          #####################
#     "PET": (100, 200),     # Apparantly the AI camera might struggle/ not work in detecting the materials itself. only glass/plastic.
#     "HDPE": (201, 300),    # I leave this here in case it can work but oh well
#     "LDPE": (301, 400),    #####################
#     "PVC": (401, 500),
#     "PP": (501, 600),
# }

# glass_data = {
#     "SLG": (100, 200),  # Soda Lime Glass
#     "BSG": (201, 300),  # Borosilicate Glass
#     "LC": (301, 400),  # Lead Crystal
#     "FQG": (401, 500),  # Fused Quartz Glass
#     "FG": (501, 600), # Flint Glass
# }  

#IR Reading 
def read_adc(channel):  # MCP3008 ADC Protocol
    irreading = adc.xfer2([1, (8 + channel) << 4, 0])
    data = ((irreading[1] & 3) << 8) + irreading[2]
    return data

def compare_readings(reading, mat_type, mat):
    if material_type == "Plastic":
        list_check = plastics_data
    elif material_type == "Glass":
        list_check = glass_data

    if mat in list_check:
        lowerbound, upperbound = list_check[mat]
        if lowerbound <= reading <= upperbound:
            print("Material accepted, pushing container into bin")
            m1f()
            time.sleep(3)
            m1s()
        else:
            print("Material rejected, returning container to door")
            m1r()
            time.sleep(3)
            m1s()
#IR Reading End

#Motor Controls
def m1f(): #Forward
    GPIO.output(fmotor1, GPIO.HIGH)
    GPIO.output(rmotor1, GPIO.LOW)

def m1r(): #Reverse
    GPIO.output(fmotor1, GPIO.LOW)
    GPIO.output(rmotor1, GPIO.HIGH)

def m1s(): #Stop
    GPIO.output(fmotor1, GPIO.LOW)
    GPIO.output(rmotor1, GPIO.LOW)

def m2f():
    GPIO.output(fmotor2, GPIO.HIGH)
    GPIO.output(rmotor2, GPIO.LOW)

def m2r():
    GPIO.output(fmotor2, GPIO.LOW)
    GPIO.output(rmotor2, GPIO.HIGH)

def m2s():
    GPIO.output(fmotor2, GPIO.LOW)
    GPIO.output(rmotor2, GPIO.LOW)

def m3f():
    GPIO.output(fmotor3, GPIO.HIGH)
    GPIO.output(rmotor3, GPIO.LOW)

def m3r():
    GPIO.output(fmotor3, GPIO.LOW)
    GPIO.output(rmotor3, GPIO.HIGH)

def m3s():
    GPIO.output(fmotor3, GPIO.LOW)
    GPIO.output(rmotor3, GPIO.LOW)
#Motor Controls end

#IR callibration
def ircallibration():
    m2r()
    m3r()
    time.sleep(2)
    m2s()
    m3s()

# def ultrasonicsensor():
#     GPIO.output(ultrasonic_trigger, GPIO.LOW)
#     time.sleep(0.1)
#     GPIO.output(ultrasonic_trigger, GPIO.HIGH)
#     time.sleep(0.00001)  # 10 microseconds