import sqlite3
'''Author= Jesse Eben Nyemitei
'''

db = "Database/Laptops.db"

'''this function connects to the database
'''
def connect(path):
    dblocation = path
    db = sqlite3.connect(dblocation)
    return db.cursor()

c = connect(db)

#getting table name
def tableNames():
    table = []
   
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_N = c.fetchall()
    for i in table_N[:]:
        table.append(i[0])
    return table  
    

'''Function loops through all data base tables and fetches similar information from a specific columns 
Parameter- table name, column name, and specific information in that column
Returns list of items under all tables
'''
def fetchData(table, column, info):
    itemsList = []
    
    for i in table:
    
        c.execute("SELECT * FROM "+i+ " WHERE " +column+" LIKE" +info)#due to the loop it takes items from a speicific column under all tables
    
        itemsList += c.fetchall()
    return itemsList




'''Function picks a specific table and fetches information from a specific column
Parameter- table name, column name, and specific information in that column
Returns list of items under a specific table
'''
def fetchData1(table, column, info):
    itemList = []
    
    for i in table:
        c.execute("SELECT * FROM " +i+ " WHERE " +column+" = " +info)
        itemList += c.fetchall()

    return itemList





'''function fetches all table names, two specific column names,information under the column names
'''
def fetchData2(table, column1, info1, column2, info2):
    itemsList = []
    
    for i in table:
    
        c.execute("SELECT * FROM "+i+ " WHERE " +column1+" = " +info1+ " AND "+ column2+" =?",(info2,))#from all tables
    
        itemsList += c.fetchall()
    return itemsList

#fetches prices based on cheap, moderate and expensive categories
def fetchOnlyPrice(table, price):
    itemsList = []
    if price == "cheap":
        for i in table:
            c.execute("SELECT * FROM "+i+ " WHERE Price_euros <= 350")#from all tables
    
            itemsList += c.fetchall()
    elif price == "moderate":
        for i in table:
            c.execute("SELECT * FROM "+i+ " WHERE  Price_euros > 350 AND Price_euros <=900")#from all tables
    
            itemsList += c.fetchall()
    elif price == "expensive":
        for i in table:
            c.execute("SELECT * FROM "+i+ " WHERE Price_euros > 900")#from all tables
    
            itemsList += c.fetchall()
    return itemsList

#fetches from a column and information under the column  along with the prices
def fetchColumnPrice(table, column1, info1, price):
    itemsList = []

    if price == "cheap":
        for i in table:
            c.execute("SELECT * FROM "+i+ " WHERE " +column1+" = " +info1+ " AND Price_euros <= 350")#from all tables
    
            itemsList += c.fetchall()
    elif price == "moderate":
        for i in table:
            c.execute("SELECT * FROM "+i+ " WHERE " +column1+" = " +info1+ " AND Price_euros > 350 AND Price_euros <=900")#from all tables
    
            itemsList += c.fetchall()
    elif price == "expensive":
        for i in table:
            c.execute("SELECT * FROM "+i+ " WHERE " +column1+" = " +info1+ " AND Price_euros > 900")#from all tables
    
            itemsList += c.fetchall()

    return itemsList

#fetches from a column and information under the column along with the brand name and price range
def fetchBrandPrice(table, column1, info1, brand, price):
    itemsList = []

    if price == "cheap":
        for i in table:
            c.execute("SELECT * FROM " +i+ " WHERE " +column1+ " = " +info1+ " AND Company =" +brand+ " AND Price_euros <= 350")#from all tables
    
            itemsList += c.fetchall()
    elif price == "moderate":
        for i in table:
            c.execute("SELECT * FROM " +i+ " WHERE " +column1+ " = " +info1+ " AND Company =" +brand+ " AND Price_euros > 350 AND Price_euros <=900")#from all tables
    
            itemsList += c.fetchall()
    elif price == "expensive":
        for i in table:
            c.execute("SELECT * FROM " +i+ " WHERE " +column1+ " = " +info1+ " AND Company =" +brand+ " AND Price_euros > 900")#from all tables
    
            itemsList += c.fetchall()

    return itemsList

#fetches all data in the data base
def fetchData4(table):
    itemsList = []
    for i in table:
    
        c.execute("SELECT * FROM %s;"% i)
    
        itemsList += c.fetchall()
    return itemsList
#fetches data from a column without repeating any item
def uniqueSelect(table,column):
    li = []
    for i in table:
        c.execute("SELECT DISTINCT " +column+ " FROM " +i)
        li += c.fetchall()#list of tuples
    return [i[0] for i in li]#looping through list of tuples


'''this function searches through the database with a specific data under a column, column name, brand and price
'''
def search(searchword="all", columname="Category", brand = "all", price = "all"):
    _word = '"'+searchword+'"'
    _brand = "'"+brand+"'"
    _brand = "'"+brand+"'"
    tables = tableNames()
    
    # given all param
    if searchword != "all" and brand != "all" and price != "all": # given all param
        return fetchBrandPrice(tables, columname, _word, _brand, price)

    # given only one param
    elif searchword != "all" and brand =="all" and price == "all": # given only searchword
        return fetchData1(tables, columname, _word)

    elif searchword == "all" and brand == "all" and price != "all": # given only price
        return fetchOnlyPrice(tables, price)

    elif searchword == "all" and brand != "all" and price == "all": # given only brand
        return fetchData1(tables, "Company", _brand)

    # given two params
    elif searchword != "all" and brand != "all" and price == "all": # given searchword and brand
        return fetchData2(tables, columname, _word, "Company", brand)

    elif searchword != "all" and brand == "all" and price != "all": # given searchword and price
        return fetchColumnPrice(tables, columname, _word, price)

    elif searchword == "all" and brand != "all" and price != "all": # given brand and price
        
        return fetchColumnPrice(tables, "Company", _brand, price)

    # given no param
    else:
        return fetchData4(tables)


    



        
            
    