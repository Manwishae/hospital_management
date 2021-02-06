import core.engine
import mysql.connector as msc
db = msc.connect(host="localhost",user="root",password="Himanshu@9506")
cursor = db.cursor(buffered=True)

database_name = "hospitalpatients"
table_name = "patients"

columns = ["ID","Name","Age","Amount","Disease"]

def create_table():
    '''This functions creates a table of fixed size and columns'''
    try:
        cursor.execute(f"create table patients({columns[0]} varchar(20) primary key, {columns[1]} varchar(50), {columns[2]} varchar(50), {columns[3]} varchar(50), {columns[4]} varchar(50))")
        db.commit()
    
    except Exception as e:
        print("Error : ",e)


def drop_table():
    '''Drops the complete table patients'''
    try:
        cursor.execute(f"drop table {table_name}")
        create_table()
        db.commit()
    
    except Exception as e:
        print("Error : ",e)

    
def select_all_from_table():
    '''Selects everything from table'''
    cursor.execute(f"select * from {table_name}")
    result = cursor.fetchall()
    return result


def insert_values(values):
    string_values = ""
    for item in values:
        if values.index(item) == 0:
            string_values += f"\"{item}\""
        else:
            string_values += f", \"{item}\""
    command = f"insert into patients values({string_values})"
    
    try:
        cursor.execute(command)
        db.commit()
        print("\nPatient Added \n")
    
    except Exception as e:
        print(e)


def select_specific_from_table(data):
    '''Selects specific patients'''
    try:
        cursor.execute(f"select * from patients where ID = \"{data}\"")
        result = cursor.fetchall()
        return result
    
    except Exception as e:
        print(e)


def drop_patient(empid):
    try:
        cursor.execute(f"delete from patients where ID = \"{empid}\"")
        
    except Exception as e:
        print(e)

try:
    cursor.execute(f"use {database_name}")
    cursor.execute(f"desc patients")

except Exception as e:
    if e.args[0] == 1049:
        cursor.execute(f"create database {database_name}")
        cursor.execute(f"use {database_name}")
        create_table()
    
    if e.args[0] == 1146:
        create_table()
    
    else:
        print(e.args)