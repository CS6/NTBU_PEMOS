#from delay import delayed
import time
import serial
i=0
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
    data = ser.readline()
#    @delayed(10)
#    def foo():
    print(data)
time.sleep(1000)
