# coding=UTF-8
import csv
import time
import serial
import MySQLdb
import time,datetime
import sys
import MySQLdb as mdb
#設定欲讀取的序列埠
ser = serial.Serial('/dev/ttyACM0', 9600)#arduino板01
sre = serial.Serial('/dev/ttyACM1', 9600)#arduino板02
#設定時間戳記&格式化日期
DD=time.strftime("%Y-%m-%d--%H:%M:%S")
DT=time.strftime("%Y-%m-%d--%H:%M:%S") 

print(DT) 

i=0
while 1 :
	
    #原始語法items = line.strip().split(' ')
    #data[陣列]=讀入一行,使用strip()去除(頭/尾)的空白,使用split(';')分割為陣列data[]
    data = ser.readline().strip().split(';')
    #data[陣列]=讀入一行,使用strip()去除(頭/尾)的空白,使用split(';')分割為陣列data[]
    datb = sre.readline().strip().split(';')
    if len(data)>2:
    	#將時間戳記加入data[陣列]的起始位置(0,時間戳記)
	    data.insert(0,DD)
	    #將時間戳記加入datb[陣列]的起始位置(0,時間戳記)
	    datb.insert(0,DT)	
	    #print "Length = ", len(data)

	    print("<----")
	    print(data)
	    print("----")
	    print(datb)
	    print("---->")

	    #開啟(csv檔,寫在後面)
	    f = open("NTBU.csv", "a")
	    #csv 寫入檔案
	    w = csv.writer(f)
	    #寫入(data)
	    w.writerow(data)
	    #寫入(datb)
	    w.writerow(datb)

	   	#關閉檔案
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
