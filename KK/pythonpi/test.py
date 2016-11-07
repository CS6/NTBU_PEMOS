import csv





import csv

import serial
i=0
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
    data = ser.readline()
      
   
    
    print(data)
    f = open("NTBU.csv", "a")
    w = csv.writer(f)
    w.writerows([data])
   
    f.close()
    
        
#CSV檔有問題，下雌嘗試LOG轉CSV