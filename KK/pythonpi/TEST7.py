# coding=UTF-8
import time
import serial
import MySQLdb
import time,datetime
import sys
import MySQLdb as mdb

ser = serial.Serial('/dev/ttyACM0', 9600)
sre = serial.Serial('/dev/ttyACM1', 9600)
print time.strftime("%Y-%m-%d%x")
i=0

data=[]
con = mdb.connect('localhost', 'sddivid', '22476103', 'python');
with con:
    cur = con.cursor()
    while(i<2):	
    	#讀入一行,使用strip()去除(頭/尾)的空白,使用split('空白')分割為序列items[]
        #items = line.strip().split(' ')
        data = ser.readline().strip().split(';')
        datb = sre.readline()
        #print "Length = ", len(data)

        # Do something with my list list 是否为空
        print(data[0:1])
        print(data[1:2])
        print(data[2:3])
        print(data[3:4])
        print(datb)
        i=i+1 

        
    cur.execute("INSERT INTO GETtemp(geth,getc,getf,getk) VALUES (data[0:1],data[1:2],data[2:3], data[3:4])")
    
print "Good bye!"







    



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