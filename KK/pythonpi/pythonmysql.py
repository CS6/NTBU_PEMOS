# coding=UTF-8

import MySQLdb

try:
	# 建立DB 連線資訊定設定中文編碼utf-8
	db = MySQLdb.connect
	("localhost","sddivid","22476103","python")

	sql = "SELECT codeA, codeB FROM coding5"

	cursor = db.cursor()
	cursor.execute(sql)

	results = cursor.fetchall()

	for record in results:
		col1 = record[0]
		col2 = record[1]

		print "%s, %s" % (col1, col2)
	db.close()


except MySQLdb.Error as e:
	print "Error %d: %s" % (e.args[0], e.args[1])