# coding=UTF-8
#!/usr/bin/env python
# Run with no args for usage instructions
#
# Notes:
#  - will probably insert duplicate records if you load the same file twice
#  - assumes that the number of fields in the header row is the same
#    as the number of columns in the rest of the file and in the database
#  - assumes the column order is the same in the file and in the database
#https://freshventure.wordpress.com/2011/02/23/%E5%88%A9%E7%94%A8python%E5%B0%86csv%E6%96%87%E4%BB%B6%E5%AF%BC%E5%85%A5mysql/
# Speed: ~ 1s/MB
# 
import sys
import MySQLdb
import csv

def main(user, pwd, db, table, csvfile):

	try:
		conn = getconn(user, pwd, db)
	except MySQLdb.Error, e:
		print "Error %d: %s" % (e.args[0], e.args[1])
		sys.exit (1)

	cursor = conn.cursor()

	loadcsv(cursor, table, csvfile)

	cursor.close()
	conn.close()

def getconn(user, pwd, db):
	conn = MySQLdb.connect(host = "localhost",user = "sddivid",passwd = "22476103",db = "python")

	return conn
def nullify(L):
	"""Convert empty strings in the given list to None."""

	# helper function
	def f(x):
		if(x == ""):
			return None
		else:
			return x

	return [f(x) for x in L]

def loadcsv(cursor, table, filename):

	"""
	Open a csv file and load it into a sql table.
	Assumptions:
	 - the first line in the file is a header
	"""

	f = csv.reader(open('UTBUtest.csv'))

	header = f.next()
	numfields = len(header)

	query = buildInsertCmd(table, numfields)

	for line in f:
		#避免多余空行影响
		if len(line)<1: continue
		vals = nullify(line)
		cursor.execute(query, vals)

	return
def buildInsertCmd(table, numfields):

	"""
	Create a query string with the given table name and the right
	number of format placeholders.

	example:
	>>> buildInsertCmd("foo", 3)
	'insert into foo values (%s, %s, %s)'
	"""
	assert(numfields > 0)
	placeholders = (numfields-1) * "%s, " + "%s"
	query = ("insert into %s" % table) + (" values (%s)" % placeholders)
	return query	
if __name__ == '__main__':
	# commandline execution

	args = sys.argv[1:]
	if(len(args) < 5):
		print "error: arguments: user \"password\" db table csvfile"
		sys.exit(1)

	main(*args)