import time, serial
import fcntl

SERIALPORT = "/dev/ttyUSB0"
BAUDRATE = 1200

ser = serial.Serial(SERIALPORT, BAUDRATE) # Constructor already opens device !

ser.bytesize = serial.EIGHTBITS
ser.parity = serial.PARITY_NONE
ser.stopbits = serial.STOPBITS_ONE
ser.timeout = None

print('[+] Starting Up Serial Monitor')

## DROPPED: Contructor already opened device ! ##
#try:
#    ser.open()
#except Exception as e:
#    print("[!] error open serial port: " + str(e))
#    exit()

if ser.isOpen():
    try:
        response = ""
        while True:
            byte = ser.read()
            response += byte.decode("utf-8")
            if byte == b'\r':
               break
        print("[+] read data is: " + str(response))
        ser.close()
    except Exception as e:
        print("[!] communication error: " + str(e))
else:
    print("[!] cannot open serial port; aborting...")


