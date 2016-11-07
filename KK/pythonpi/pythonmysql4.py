#!/usr/bin/python

import serial
import MySQLdb

#establish connection to MySQL. You'll have to change this for your database.
dbConn = MySQLdb.connect('localhost', 'sddivid', '22476103', 'python') or die ("could not connect to database")

#open a cursor to the database
cursor = dbConn.cursor()

device = '/dev/ttyACM0' #this will have to be changed to the serial port you are using
try:
	print "Tryin4g...",device
	arduino = serial.Serial(device, 9600)
except:
	print "Failed to connect on",device

try:
	data = arduino.readline()
	pieces = data.split("\t")
	try:
		cursor.execute("INSERT INTO weatherData (humidity,tempC) VALUES (%s,%s)", (pieces[0],pieces[1]))
		dbConn.commit()
		cursor.close()
		print data
	except MySQLdb.IntegrityError:
		print "failed to insert data"
	finally:
		cursor.close()
except:
	print "Failed to get data from Arduino!"
	print data

