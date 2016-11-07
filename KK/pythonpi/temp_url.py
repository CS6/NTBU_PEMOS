#!/usr/bin/env python
# author: Powen Ko
import time
import urllib
import serial
def fetch_thing(rul, parms, method):
	params = urllib.urlencode(params)
	if method=='POST':
		f=urllib.urlopen(url,params)
	else:
		f=urllib.urlopen(url+'?'+params)
	return (f.read(), f.code)
print('AA')
i=0
ser = serial.Serial('/dev/ttyACM0', 9600)
print('BB')

	
data = ser.readline()
      
print('CC')    
total=data
temp=total;
print(data)
print('DD')  
content,response_code = fetch_thing('http://106.104.114.80/settemp.php',{'id': 1,'temp':temp},'GET')
print('EE')  