import mysql.connector as msc
db = msc.connect(host="localhost",user="root",password="Himanshu@9506")
cursor = db.cursor()

''' This file is related to database handling and management'''

database_name = "hopitalpatients"

def createDatabase():
    '''Creates database if doesnot exists'''
    cursor.execute(f"create database {database_name}")

def testDatabase():
    '''Checks wether database is available or not'''
    try:
        cursor.execute(f"use {database_name}")
        return True

    except Exception as e:
        if e.args[0] == 1049:
            createDatabase()
        else:
            print(e)
            return False

def removeDatabase():
    '''Removes the database'''
    cursor.execute(f"drop database {database_name}")

def useDatabase():
    '''use the available database'''
    available = testDatabase()