# -*- coding: UTF-8 -*-
# coding=UTF-8

#mysqldb	 
import MySQLdb
import sys
import serial
import time
import csv
import time,datetime
#設定欲讀取的序列埠
ser = serial.Serial('/dev/ttyACM0', 9600)#arduino板01
sre = serial.Serial('/dev/ttyACM1', 9600)#arduino板02
#設定時間戳記&格式化日期
DD=time.strftime("%Y-%m-%d--%H:%M:%S")
DT=time.strftime("%Y-%m-%d--%H:%M:%S") 

print(DT) 
#http://drizzlewalk.blog.51cto.com/2203401/448874
#连接	 
conn=MySQLdb.connect(host="localhost",user="sddivid",passwd="22476103",db="python",charset="utf8")  
cursor = conn.cursor()	 

#写入	 
#sql = "insert into DDDDD(name,created) values(%s,%s)"	
#param = ("aaa",int(time.time()))	 
#DD= cursor.execute(sql,param)	 
#print DD

while 1 :
	
    #原始語法items = line.strip().split(' ')
    #data[陣列]=讀入一行,使用strip()去除(頭/尾)的空白,使用split(';')分割為陣列data[]
    data = ser.readline().strip().split(';')
    #data[陣列]=讀入一行,使用strip()去除(頭/尾)的空白,使用split(';')分割為陣列data[]
    datb = sre.readline().strip().split(';')
    if len(data)>2:


    	sql="insert into GETtemp values(0,%s,%s,%s,%s)"
		param=data
		n=cursor.execute(sql,param)
		print n
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
	    f = open("NTBUtest.csv", "a")
	    #csv 寫入檔案
	    w = csv.writer(f)
	    #寫入(data)
	    w.writerow(data)
	    #寫入(datb)
	    w.writerow(datb)

	   	#關閉檔案
	    f.close()

print "Good bye!"

conn.commit()
conn.close()
####


#如果需要批量的插入数据,就这样做
#sql="insert into ASD values(0,%s,%s,%s,%s,%s)"
#每个值的集合为一个tuple,整个参数集组成一个tuple,或者list:(geth,getc,getf,getk)
#param=((title,singer,imgurl,url))
#使用executemany方法来批量的插入数据.这真是一个很酷的方法!
#n=cursor.executemany("insert into  GETtemp values(%s,%s,%s,%s)",param)
#sql="insert into GETtemp values(0,%s,%s,%s,%s)"

#每个值的集合为一个(tuple),整个参数集组成一个(tuple),或者(list)
#用法為param=([list],(tuple))
#param=(A,(title2,singer2,imgurl2,url2))
#使用executemany方法来批量(2組以上)的插入数据.这真是一个很酷的方法! 
#n=cursor.executemany(sql,param)

#param的資料只能为一个(tuple)或者(list)
#用法為param=[list]或是param=(tuple)
#使用execute方法(只能1組)的插入数据
#n=cursor.executemany(sql,param)




###################################!!!BUG只會上傳資料!!!!!!#######################################

###################################!!!print n後直接結束!!!!!!#######################################