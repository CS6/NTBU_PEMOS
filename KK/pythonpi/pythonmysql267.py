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

sql = "insert into myTable (created_day,name,count) values(%s,%s,%s) ON DUPLICATE KEY UPDATE count=count+values(count)"
args=[("2012-08-27","name1",100),("2012-08-27","name1",200),("2012-08-27","name2",300)] 
try:
	cursor.executemany(sql,args)
except Exception as e:
	print 0("执行Mysql: %s 时出错：%s" % (sql,e))
finally: 
	cursor.close()
	conn.commit()
	conn.close()


#如果需要批量的插入数据,就这样做http://lengyue318.iteye.com/blog/1664367
#sql="insert into ASD values(0,%s,%s,%s,%s,%s)"
#每个值的集合为一个tuple,整个参数集组成一个tuple,或者list:(geth,getc,getf,getk)
#param=((title,singer,imgurl,url))
#使用executemany方法来批量的插入数据.这真是一个很酷的方法!
#n=cursor.executemany("insert into  GETtemp values(%s,%s,%s,%s)",param)
#sql="insert into GETtemp values(0,%s,%s,%s,%s)"
#每个值的集合为一个tuple,整个参数集组成一个tuple,或者list 
#param=((title,singer,imgurl,url),(title2,singer2,imgurl2,url2))
#使用executemany方法来批量的插入数据.这真是一个很酷的方法! 
#n=cursor.executemany(sql,param)
