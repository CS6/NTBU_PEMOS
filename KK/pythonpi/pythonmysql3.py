# -*- coding: UTF-8 -*-
	
import MySQLdb as mdb
import sys
import serial
i=0
ser = serial.Serial('/dev/ttyACM0', 9600)
data = ser.readline()
    
  
    

con = mdb.connect('localhost', 'sddivid', '22476103', 'python');
	
with con:
	

	cur = con.cursor()

	cur.execute("CREATE TABLE IF NOT EXISTS \
		getQQ(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(50))")
	

	
	cur.execute("INSERT INTO getQQ(Name) VALUES(data)")
	


print "Good bye!"

