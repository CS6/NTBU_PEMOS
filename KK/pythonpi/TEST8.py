# coding=UTF-8
import time
import serial
import MySQLdb
import time,datetime
import sys
import MySQLdb as mdb
import urllib

def fetch_thing(rul, parms, method):
    params = urllib.urlencode(params)
    if method=='POST':
        f=urllib.urlopen(url,params)
    else:
        f=urllib.urlopen(url+'?'+params)
    return (f.read(), f.code)
print('AA')

ser = serial.Serial('/dev/ttyACM0', 9600)
sre = serial.Serial('/dev/ttyACM1', 9600)
print time.strftime("%Y-%m-%d%x")

while(1):	
    #讀入一行,使用strip()去除(頭/尾)的空白,使用split('空白')分割為序列items[]
    #items = line.strip().split(' ')
    data = ser.readline().strip().split(';')
    datb = sre.readline()
    #print "Length = ", len(data)

    # Do something with my list list 是否为空
    D0=data[0:1]
    D1=data[1:2]
    D2=data[2:3]
    D3=data[3:4]
    print(D0)
    print(D1)
    print(D2)
    print(D3)
    print(datb)
    getH=D0
    temp=D1
    if (getH>0):
        
        print(data)
        print data[0:1],data[1:2],data[2:3],data[3:4]  
        content,response_code = fetch_thing('http://106.104.114.80//settemp.php',{'id': 1,'temp':temp},'GET')
    else:
        print('EE')  

        

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