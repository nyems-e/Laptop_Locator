'''This is the backend code for my project. It aims at connecting and fetching data
from my data base of laptops and provides a foundation
for the GUI I will be creating to help provide the search
functionality of the program I am creating'''

'''Author: Jesse Eben Nyemitei
Semester Project
'''
import sqlite3


#Connecting to database
d = "Database/TRS.db"
db = sqlite3.connect(d)
c = db.cursor()

    


#getting all database tables
def tableNames():
    table = []
   
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_N = c.fetchall()
    for i in table_N[1:]: 
        table.append(i[0])

    return table   
    

'''Function loops through all data base tables and fetches similar information from specfic columns
Parameter- table name, column name, and specific information in that column
Returns list of items under all tables
'''
def fetchData(table, column, info):
    itemsList = []
    
    for i in table:
    
        c.execute("SELECT * FROM "+i+ " WHERE " +column+" LIKE " +info)#due to the loop it takes items from a speicific column under all tables
    
        itemsList += c.fetchall()
    return itemsList




'''Function picks a specific table and fetches information from a specific column
Parameter- table name, column name, and specific information in that column
Returns list of items under a specific table
'''
def fetchData1(table, column, info):
    itemList = []
    
    c.execute("SELECT * FROM " +table+ " WHERE " +column+" LIKE " +info)#selects items from a specific column under only one table
    itemList += c.fetchall()
    return itemList





'''function fetches all table names, specfic column name,information under the column name and release date column name
Parameter- table name, specific column name(can vary), information under that specific column name, release Date
'''
def fetchData2(table, column, info, releaseDate):
    itemsList = []
    
    for i in table:
    
        c.execute("SELECT * FROM "+i+ " WHERE " +column+" LIKE " +info+ " AND Release_Date =?",(releaseDate,))#from all tables
    
        itemsList += c.fetchall()
    return itemsList




'''function fetches a specific table name, specific column name, information under the column name, release date colum name
Parameter- table name, column name, infprmation under column name, release date column name
'''
def fetchData3(table, column, info, releaseDate):
    itemList = []
    
    c.execute("SELECT * FROM "+table+ " WHERE " +column+" LIKE " +info+ " AND Release_Date =?",(releaseDate,))#from one table
    
    itemList += c.fetchall()
    return itemList


def fetchData4(table):
    itemsList = []
    for i in table:
    
        c.execute("SELECT * FROM %s;"% i)
    
        itemsList += c.fetchall()
    return itemsList

def fetchData5(table):
    itemsList = []
    
    c.execute("SELECT * FROM %s;"% table)
    
    itemsList = c.fetchall()
    return itemsList


def fetchData6(table,releaseDate):
    itemsList = []
    
    c.execute("SELECT * FROM "+table+ " WHERE Release_Date =?",(releaseDate,))
    
    itemsList += c.fetchall()
    return itemsList

def fetchData7(table,releaseDate):
    itemsList = []
    for i in table:
        c.execute("SELECT * FROM "+i+ " WHERE Release_Date =?",(releaseDate,))
    
    itemsList += c.fetchall()
    return itemsList
    

#function searches with a specific searchword which is specific data under the category column, brand which refers to the table names and release date

def search(searchword="all", brand = "all", releaseDate = "all"):
    word = "'%"+searchword+"%'"
    tables = tableNames()
    
     
    if searchword != "all" and (brand == "all" and releaseDate == "all"):
       data = fetchData(tables, "Category", word)#gives caategory type under each laptop
       return data
    elif brand != "all" and  searchword != "all" and releaseDate == "all":#gives category under only one table
        data = fetchData1(brand,"Category", word)
        return data
    elif brand == "all" and releaseDate != "all" and  searchword != "all":#gives category under each table wth a specific release date
        data = fetchData2(tables,"Category", word, releaseDate)
        return data
    elif brand != "all" and releaseDate != "all" and  searchword != "all":
        data = fetchData3(brand, "Category",word,releaseDate)
        return data
    elif brand != "all" and releaseDate == "all" and  searchword == "all":
        data = fetchData5(brand)
        return data
    elif releaseDate != "all" and brand != "all" and searchword == "all":
        data = fetchData6(brand,releaseDate)
        return data
    elif releaseDate != "all" and (brand == "all" and searchword == "all"):
        data = fetchData7(tables,releaseDate)
        return data
    else:
        data = fetchData4(tables)
        return data
        
            
    

    
  
    
    
     
   
    
    
    
    
    
    
    
    




    




