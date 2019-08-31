import sqlite3
##its important to know what the names of the databases that have been created
##this means the user cant unknowingly overwrite a database
def getdatabases():
    databaseList = open("databaseList.txt", 'r')
    results = databaseList.readlines()
    databaseList.close()
    for i in range(len(results)):
        print("--" + results[i])

def createDB():
    print()
    print("the following are the names of existing databases")
    print("-------------------------")
    getdatabases()##list all detabases that exist
    print("-------------------------")
    print()
    ##get user input
    print("please enter a name for your database, without front or back slashes")
    print("entering a name of a pre-existing database will wipe it")
    name = input()
    database = sqlite3.connect(name)##this creats a database named using the characters inputed
    print("database successfully created")
