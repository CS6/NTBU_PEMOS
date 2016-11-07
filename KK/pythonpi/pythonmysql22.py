# -*- coding: UTF-8 -*-
	
import MySQLdb as mdb
import sys
import serial
import time,datetime
ser = serial.Serial('/dev/ttyACM0', 9600)
data = ser.readline()
con = mdb.connect('localhost', 'sddivid', '22476103', 'python');
DTtime=time.strftime("%Y-%m-%d%x")
with con:

	cur = con.cursor()

	#cur.execute("CREATE TABLE IF NOT EXISTS \
	#	GETtemp(Id INT PRIMARY KEY AUTO_INCREMENT, geth VARCHAR(50),getc VARCHAR(50),getf VARCHAR(50),getk VARCHAR(50)")

	cur.execute("INSERT INTO GETtemp(geth,getc,getf,getk) VALUES ('111','25','25', '222')")

	