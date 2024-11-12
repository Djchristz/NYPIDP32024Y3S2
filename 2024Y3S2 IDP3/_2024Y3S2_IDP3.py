# import spidev
import time

##########################################
# Whack all the GPIO Pins here, lazy anyhow define
#########################################

# ADC setup (example for MCP3008 on SPI interface)
# spi = spidev.SpiDev()
# spi.open(0, 0)  # Open on bus 0, device 0
# spi.max_speed_hz = 1350000

global scan_mat_type
global scan_mat

plastics_data = {
    "PET": (100, 200),
    "HDPE": (201, 300),
    "LDPE": (301, 400),
    "PVC": (401, 500),
    "PP": (501, 600),
}

glass_data = {
    "SLG": (100, 200),  # Soda Lime Glass
    "BSG": (201, 300),  # Borosilicate Glass
    "LC": (301, 400),  # Lead Crystal
    "FQG": (401, 500),  # Fused Quartz Glass
    "FG": (501, 600), # Flint Glass
}  

def read_adc(channel):  # MCP3008 ADC Protocol
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
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
            # Conveyor push to bin
        else:
            print("Material rejected, returning container to door")
            |# Conveyor returns


# Main loop
try:
    while True:
        ####################
        #Blah Blah Code for everything else
        ####################

        #IR Receiver code
        compare_readings(read_adc(0),scan_mat_type,scan_mat) #Read ADC check what channel receiver connected to 


except KeyboardInterrupt:
    print("Program interrupted by user.")
# finally:
    # spi.close()