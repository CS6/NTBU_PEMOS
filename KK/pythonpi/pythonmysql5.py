# -*- coding: utf-8 -*-
import serial



port = serial.Serial('/dev/ttyACM0', 9600)   #設定路徑、鮑率、時間


port.flushInput()  #更新port丟棄接收緩存中的所有數據



def receiving(port):                                                 #接收Arduio資料，處理後回傳

    global last_received #存取全域變數



    buffer_string = ''

    while True:

        buffer_string = buffer_string + "".join(map(chr,port.read(port.inWaiting()))) #返回接收緩存中的字節數
        print (last_received)   

        if '\n' in buffer_string:

            lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries

            last_received = lines[-2]

            #If the Arduino sends lots of empty lines, you'll lose the

            #last filled line, so you could make the above statement conditional

            #like so: if lines[-2]: last_received = lines[-2]

            buffer_string = lines[-1]

            return last_received
    print (last_received)       



def getdata(port):                                                   #將多重數據分割後回傳

    try:

        data = receiving(port)

        data_split = data.split()

        return data_split

    except:

        print("fail") 


def getitem(port): 
    while True:

        data1=getdata(port)  

        if data1 != "fail":

            temperature = data1[0]

            humidity = data1[1]

            illuminance =data1[2] 

            soilmoisture =data1[3]         

            print(temperature+""+ humidity+""+illuminance+""+soilmoisture)         #顯示數據

        else: 

            print("false")
