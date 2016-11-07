# -*- coding: UTF-8 -*-

#! /usr/bin/python
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import MySQLdb.connector
from MySQLdb.connector.constants import ClientFlag
from MySQLdb.connector.constants import SQLMode
import MySQLdbdb

MySQLdb_config = {
    'host':'localhost',
    'user':'sddivid',
    'password':'22476103',
    'port':3306,
    'database':'python',
    'charset':'utf8',
    'client_flags':[ClientFlag.LOCAL_FILES],
}

def isset(v):
    try:
        type (eval(v))
    except:
        return False
    else:
        return True

def LoadFile():
    try:
        cnn = MySQLdb.connector.connect(**MySQLdb_config)

        sql = "LOAD DATA LOCAL INFILE '/etc/workspace/NTBUtest.csv' REPLACE INTO TABLE test FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
        cursor = cnn.cursor()
        cursor.execute(sql)
        cnn.commit()
    except MySQLdb.connector.Error as e:
        print('LoadFile sql fails {}'.format(e))
    finally:
        if isset("cursor"):
            cursor.close()
        if isset("cnn"):
            cnn.close()

def LoadFile2():
    cnn = MySQLdbdb.connect(host="localhost", user="sddivid", passwd="22476103", db="python", charset="utf8")
    cursor = cnn.cursor()
    sql = "LOAD DATA LOCAL INFILE '/etc/workspace/NTBUtest.csv' REPLACE INTO TABLE test FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
    cursor.execute(sql)
    cnn.commit()

if __name__ == "__main__":
#    LoadFile()
    LoadFile2()
