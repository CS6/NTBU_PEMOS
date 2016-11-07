# -*- coding: UTF-8 -*-
import MySQLdb
import xlrd
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# 从users.xls文件获取10000条用户数据
# 该文件由create_users.py生成
def get_table():
	FILE_NAME = 'users.xls'
	data = xlrd.open_workbook(FILE_NAME)
	table = data.sheets()[0]
	return table

# 循环插入execute	 
def insert_by_loop(table):
	nrows = table.nrows
	for i in xrange(1,nrows):
		param=[]
		try:
			sql = 'INSERT INTO user values(%s,%s,%s)'
			# 第一列username，第二列salt，第三列pwd
			print 'Insert: ',table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 2).value
			param = (table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 2).value)
			# 单条插入
			cur.execute(sql, param)
			conn.commit()
		except Exception as e:
			print e
			conn.rollback()
	print '[insert_by_loop execute] total:',nrows-1

# 批量插入executemany
def insert_by_many(table):
	nrows = table.nrows
	param=[]
	for i in xrange(1,nrows):
		# 第一列username，第二列salt，第三列pwd
		param.append([table.cell(i, 0).value, table.cell(i, 1).value, table.cell(i, 2).value])
	try:
		sql = 'INSERT INTO user values(%s,%s,%s)'
		# 批量插入
		cur.executemany(sql, param)
		conn.commit()
	except Exception as e:
		print e
		conn.rollback() 
	print '[insert_by_many executemany] total:',nrows-1 


# 连接数据库
conn = MySQLdb.connect(host="127.0.0.1", port=3306, user="lrg", passwd="lrg", db="pythontest")
cur = conn.cursor()

# 新建数据库
cur.execute('DROP TABLE IF EXISTS user')
sql = """CREATE TABLE user( 
		username CHAR(255) NOT NULL, 
		salt CHAR(255), 
		pwd CHAR(255) 
		)"""
cur.execute(sql)

# 从excel文件获取数据
table = get_table()
	
# 使用循环插入
start = time.clock()
insert_by_loop(table)
end = time.clock()
print '[insert_by_loop execute] Time Usage:',end-start

# 使用批量插入
start = time.clock()
insert_by_many(table)
end = time.clock()
print '[insert_by_many executemany] Time Usage:',end-start

# 释放数据连接
if cur:
	cur.close()
if conn:
	conn.close()