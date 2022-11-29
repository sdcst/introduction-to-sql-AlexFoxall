#!python

"""
Create a program that will store the database for a veterinary
Each record needs to have the following information:
id unique integer identifier
pet name
pet species (cat, bird, dog, etc)
pet breed (persian, beagle, canary, etc)
owner name
owner phone number
owner email
owner balance (amount owing)
date of first visit

create a program that will allow the user to:
insert a new record into the database and save it automatically
retrieve a record by their id and display all of the information
retrieve a record by the email and display all of the information
retrieve a record by phone number and display all of the information

You will need to create the table yourself. Consider what data types you will
need to use.
"""
import sqlite3
def add():
    file = 'assignment.db'
    connection = sqlite3.connect(file)
    print(connection)
    cursor = connection.cursor()
    x = input('pet name')
    c = input('pet species')
    v = input('pet breed')
    b = input('owner name')
    n = input('owner phone number')
    m = input('owner email')
    a = input('owner balance')
    s = input('date of first visit(mm/dd/yy)')
    data = [x,c,v,b,n,m,a,s]

    query = """
    create table if not exists customers (
        id integer primary key autoincrement,
        pet tinytext,
        species tinytext,
        breed tinytext,
        name tinytext,
        phone tinytext,
        email tinytext,
        balance int,
        date tinytext
        );
    """
    cursor.execute(query)


    query = f"insert into customers (pet,species,breed,name,phone,email,balance,date) values ('{x}','{c}','{v}','{b}','{n}','{m}',{a},'{s}');"
    print(query)
    cursor.execute(query)
    connection.commit()
    return

def findid():
    file = 'assignment.db'
    connection = sqlite3.connect(file)
    print(connection)
    x = input('enter name')
    cursor = connection.cursor()
    query = "select name from customers"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    return
findid()