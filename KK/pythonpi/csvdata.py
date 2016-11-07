import csv
import datetime
from datetime import datetime
from time import strftime
fileDT = datetime.now().strftime('%Y%m%d_%H%M%S')
#fileID =datetime.now().strftime('%Y%m%d')


import csv
#from delay import delayed
import time
import serial
i=0
ser = serial.Serial('/dev/ttyACM0', 9600)
while 1 :
    data = ser.readline()
    #time.sleep(1000)
    print(data)    
    f = open(fileDT +".csv", "wb")
    w = csv.writer(f)
    w.writerows(fileDT)
    w.writerows(data)
    f.close()    

    
    
