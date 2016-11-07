# -*- coding: UTF-8 -*-
	
import MySQLdb as mdb
import sys
	
con = mdb.connect('localhost', 'sddivid', '22476103', 'python');
	
with con:

	cur = con.cursor()

	#cur.execute("CREATE TABLE IF NOT EXISTS \
		#temp(Id INT PRIMARY KEY AUTO_INCREMENT, temp VARCHAR(50))")

	cur.execute("INSERT INTO temp(temp) VALUES('Jack London')")
	cur.execute("INSERT INTO temp(temp) VALUES('Honore de Balzac')")
	cur.execute("INSERT INTO temp(temp) VALUES('Lion Feuchtwanger')")
	cur.execute("INSERT INTO temp(temp) VALUES('Emile Zola')")
	cur.execute("INSERT INTO temp(temp) VALUES('Truman Capote')")
	cur.execute("INSERT INTO temp(temp) VALUES('Jack London')")
	cur.execute("INSERT INTO temp(temp) VALUES('Honore de Balzac')")
	cur.execute("INSERT INTO temp(temp) VALUES('Lion Feuchtwanger')")
	cur.execute("INSERT INTO temp(temp) VALUES('Emile Zola')")
	cur.execute("INSERT INTO temp(temp) VALUES('Truman Capote')")
	cur.execute("INSERT INTO temp(temp) VALUES('Jack London')")
	cur.execute("INSERT INTO temp(temp) VALUES('Honore de Balzac')")
	cur.execute("INSERT INTO temp(temp) VALUES('Lion Feuchtwanger')")
	cur.execute("INSERT INTO temp(temp) VALUES('Emile Zola')")
	cur.execute("INSERT INTO temp(temp) VALUES('Truman Capote')")
	cur.execute("INSERT INTO temp(temp) VALUES('Jack London')")
	cur.execute("INSERT INTO temp(temp) VALUES('Honore de Balzac')")
	cur.execute("INSERT INTO temp(temp) VALUES('Lion Feuchtwanger')")
	cur.execute("INSERT INTO temp(temp) VALUES('Emile Zola')")
	cur.execute("INSERT INTO temp(temp) VALUES('Truman Capote')")