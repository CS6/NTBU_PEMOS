# -*- coding: UTF-8 -*-
import csv
import time
import sys
import MySQLdb as mdb
import serial
import time,datetime
con = mdb.connect('localhost', 'sddivid', '22476103', 'python');
ser = serial.Serial('/dev/ttyACM0', 9600)#arduino板01
sre = serial.Serial('/dev/ttyACM1', 9600)#arduino板02
#設定時間戳記&格式化日期
DD=time.strftime("%Y-%m-%d--%H:%M:%S")
DT=time.strftime("%Y-%m-%d--%H:%M:%S") 
data = ser.readline().strip().split(';')
#data[陣列]=讀入一行,使用strip()去除(頭/尾)的空白,使用split(';')分割為陣列data[]
datb = sre.readline().strip().split(';')

#value=[1,'hi rollen']
with con:

	cur = con.cursor()
	#load data infile '/etc/workspace/NTBUtest.csv' into table user('username', 'salt','pwd')
	#"LOAD DATA LOCAL INFILE 'etc\\workspace\\NTBUtest.csv' \
INTO TABLE stock CHARACTER SET 'utf8'\
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' \
LINES TERMINATED BY '\\r\\n' \
IGNORE 1 LINES (saledate, stockkind, stockid ,openprice, highprice, lowprice, lastprice, brokerid, price, buyvol, sellvol);"
	#cur.execute("CREATE TABLE IF NOT EXISTS \
	#	GETtemp(Id INT PRIMARY KEY AUTO_INCREMENT, geth VARCHAR(50),getc VARCHAR(50),getf VARCHAR(50),getk VARCHAR(50)")

	#cur.execute("INSERT INTO GETtemp(geth,getc,getf,getk) VALUES (i,j,x,y)")
	#cur.execute('insert into GETtemp values(%s,%s)',value)