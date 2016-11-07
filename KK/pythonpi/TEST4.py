import time
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
sre = serial.Serial('/dev/ttyACM1', 9600)
while 1 :
	
    data = ser.readline()
    datb = sre.readline()
    print(data)
    print(datb)
    file = open('test.txt','a')
    file.write(data)
    file.write(datb)
    file.close()




