# -*- coding: UTF-8 -*-

#mysqldb	 
import MySQLdb
import sys
import serial
import time
#http://drizzlewalk.blog.51cto.com/2203401/448874
ser = serial.Serial('/dev/ttyACM0', 9600)
data = ser.readline()
#conn = mdb.connect('localhost', 'sddivid', '22476103', 'python');
DTtime=time.strftime("%Y-%m-%d%x")

#连接	 
conn=MySQLdb.connect(host="localhost",user="sddivid",passwd="22476103",db="python",charset="utf8")  
cursor = conn.cursor()	 

#写入	 
#sql = "insert into DDDDD(name,created) values(%s,%s)"	
#param = ("aaa",int(time.time()))	 
#DD= cursor.execute(sql,param)	 
#print DD
title=34
singer=55
imgurl=86
url=9
title2=7
singer2=7
imgurl2=7
url2=7
#A=(title,singer,imgurl,url)
A=[title,singer,imgurl,url]

#如果需要批量的插入数据,就这样做
#sql="insert into ASD values(0,%s,%s,%s,%s,%s)"
#每个值的集合为一个tuple,整个参数集组成一个tuple,或者list:(geth,getc,getf,getk)
#param=((title,singer,imgurl,url))
#使用executemany方法来批量的插入数据.这真是一个很酷的方法!
#n=cursor.executemany("insert into  GETtemp values(%s,%s,%s,%s)",param)
sql="insert into GETtemp values(0,%s,%s,%s,%s)"
#每个值的集合为一个(tuple),整个参数集组成一个(tuple),或者(list)
#用法為param=([list],(tuple))
#param=(A,(title2,singer2,imgurl2,url2))
#使用executemany方法来批量(2組以上)的插入数据.这真是一个很酷的方法! 
#n=cursor.executemany(sql,param)

#param的資料只能为一个(tuple)或者(list)
#用法為param=[list]或是param=(tuple)
#使用execute方法(只能1組)的插入数据
#n=cursor.executemany(sql,param)
param=A
n=cursor.execute(sql,param)

print n
conn.commit()
conn.close()