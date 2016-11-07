##
##  filename: demoCore.py
##

import os
import serial
CURRENTDIR = os.path.dirname(__file__)
BASEDIR = os.path.dirname(CURRENTDIR)


last_received = ''

import datetime

class DemoCore():

    def index(self,request):
        ser = serial.Serial('/dev/ttyACM0', 9600)

        data = self.receiving(ser)             
        
        html = self.showDemoHTML(data)
        return html

    def receiving(self, ser):
        global last_received
        # global ser

        buffer = ''
        while True:
            buffer = buffer + ser.read()
            if '\r\n' in buffer:
                tempbuffer = buffer.split('\r\n')
                buffer = tempbuffer[1]
                while True:
                    buffer = buffer + ser.read()
                    if '\r\n' in buffer:
                        tempbuffer = buffer.split('\r\n')
                        buffer = tempbuffer[0]                    
                        return buffer

    def showDemoHTML(self,data):
        ## reads an html file and does things with it
        ## there are better ways, but they are more complicated

        today = datetime.datetime.today()
        aDate = datetime.datetime.strftime(today,"%Y-%m-%d %H:%M:%S")

        f = open(CURRENTDIR +"/demo.html")
        html = f.read()
        html = html.replace("%TodaysDate%",aDate)
        html = html.replace("%ArduinoOutput%",str(data))

        return html

if __name__ == "__main__":
    print "Hello World";