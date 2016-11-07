# -*- coding: utf-8 -*-
import MySQLdb
def InsertData(TableName,dic):
	try:
		conn=MySQLdb.connect('localhost','sddivid','22476103','python')
		cur=conn.cursor()
		COLstr=''
		ROWstr=''
		ColumnStyle=' VARCHAR(20)'
		for key in dic.keys():
			COLstr=COLstr+' '+key+ColumnStyle+','
        	ROWstr=(ROWstr+'"%s"'+',')%(dic[key])
		try:
			cur.execute("SELECT * FROM  %s"%(TableName))
			cur.execute("INSERT INTO %s VALUES (%s)"%(TableName,ROWstr[:-1]))   
		except MySQLdb.Error,e:
			cur.execute("CREATE TABLE %s (%s)"%(TableName,COLstr[:-1]))
			cur.execute("INSERT INTO %s VALUES (%s)"%(TableName,ROWstr[:-1]))
	    	conn.commit()
	    	cur.close()
	    	conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])
if __name__=='__main__':
	dic={"a":"b","c":"d"}
	InsertData('testtable',dic)