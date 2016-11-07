# coding=UTF-8
import time
import serial
import MySQLdb
import time,datetime
import sys
import MySQLdb as mdb


print time.strftime("%Y-%m-%d%x")


con = mdb.connect('localhost', 'sddivid', '22476103', 'python');
with con:
	cur = con.cursor()
	ser = serial.Serial('/dev/ttyACM0', 9600)
   	data = ser.readline().strip().split(';')
   	print(data[0:1])
   	print(data[1:2])
   	print(data[2:3])
   	print(data[3:4])
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