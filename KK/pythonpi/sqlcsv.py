import csv
import MySQLdb
conn=MySQLdb.connect(host='localhost',user = 'python', passwd='22476103')
cur=conn.cursor()
cur.execute('CREATE SCHEMA IF NOT EXISTS Demo')
cur.execute('USE Demo')
#cur.execute('DROP TABLE IF EXISTS T1')
cur.execute('''CREATE TABLE T1
	(
	Sub INTEGER NOT NULL,
	Gender INTEGER,
	Age FLOAT,
	Education INTEGER
	)''')
Generaldata = csv.reader(file('General.csv'))
for row in Generaldata:
    cur.execute('''INSERT INTO T1
    	VALUES(%s,%s,%s,%s)''',
       	(row)
       	)
conn.commit()    
