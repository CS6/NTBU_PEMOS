#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import serial
data=""
data=""
sera=serial.Serial("/dev/ttyACM0",9600)
serb=serial.Serial("/dev/ttyACM1",9600)

sera.flushInput()
sera.flushOutput()
serb.flushInput()
serb.flushOutput()

def recv(serial):
	while True:
		data=sera.read(1)
		datb=serb.read(1)
		if data=="":
			continue
		while 1:
			n=sera.inWaiting()
			#print n
			if n>0:
				data+=sera.read(n)
				time.sleep(0.1)
			else:
				break
		return data
		if datb=="":
			continue
		while 1:
			n=serb.inWaiting()
			#print n
			if n>0:
				datb+=serb.read(n)
				time.sleep(0.1)
			else:
				break
		return datb
def main():
	while True:  
		try:  
			data=recv(sera)  
			print data
			sera.flushInput()  
			send=raw_input("input your message to Mr. Arduino:")  
			sera.write(send)
			
			#data=recv(ser)  
			#print data  
		except KeyboardInterrupt:  
			sera.close()
			serb.close()  
if __name__=="__main__":  
	main()


##可以回傳命令開關