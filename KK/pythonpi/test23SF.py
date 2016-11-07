# coding=UTF-8
import csv
import time
import serial
import MySQLdb
import time,datetime
import sys
import MySQLdb as mdb

ser = serial.Serial('/dev/ttyACM0', 9600)
sre = serial.Serial('/dev/ttyACM1', 9600)
DT=time.strftime("%Y-%m-%d%x")
print(DT) 

i=0
while 1 :
	#讀入一行,使用strip()去除(頭/尾)的空白,使用split('空白')分割為序列items[]
    #items = line.strip().split(' ')
    data = ser.readline().strip().split(';')
    datb = sre.readline().strip().split(';')
    if len(data)>2:
    	
    	

	    datc=DT,data
	    datd=DT,datb
	    datf=datb.insert(0,DT)	
	    #print "Length = ", len(data)

	    print(data[0:1])
	    print(data[1:2])
	    print(data[2:3])
	    print(data[3:4])
	    print(datb)
	    print(datc)
	    print(datd)
	    print(datf)


	    f = open("NTBU.csv", "a")
	    w = csv.writer(f)
	    w.writerow(data)
	    w.writerow(datb)
	    w.writerow(datc)
	    w.writerow(datd)
	   	
	    f.close()
	    
print "Good bye!"



#w.writerow(data)
#w.writerow(datb)
#w.writerow(datc)
#w.writerow(datd)
#46.00,26.00,78.80,299.15,13.47,13.51,1,399,0,/n
#49.00,26.00,78.80,299.15,14.45,14.48,0,240,0,
#2016-11-0311/03/16,"['46.00', '26.00', '78.80', '299.15', '13.47', '13.51', '1', '399', '0', '/n']"
#2016-11-0311/03/16,"['49.00', '26.00', '78.80', '299.15', '14.45', '14.48', '0', '240', '0', '']"

	







    



#	"""#['45.00', '26.00', '78.80', '299.15', '13.13', '13.17', '1', '399', '0', '/n']
#	###"""'''"""["濕度Humidity (%);
#	攝氏Temperature (oC);
#	華氏Temperature (oF);
#	克氏溫標Temperature (K);
#	露点温度Dew Point (oC);
#	露点温度Dew Point Slow (oC);
#	麥克風數字值 Mic Digital Value;
#	 煙霧類比Smoke A Value;
#	 煙霧數位Smoke D Value;"]
#	"""        
