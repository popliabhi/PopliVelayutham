# Dao.py 
import mysql.connector
import Model as m

def connector():
    cnx = mysql.connector.connect(user='root',
                                  password='#Patran92',
                                  host='127.0.0.1',
                                  database='day2db')

    return cnx

def readByIdBreed(IDs):
    cnx = connector()
    mycursor = cnx.cursor()
    sql = "SELECT * FROM breed WHERE id = %s"
    idlist = [str(IDs)]
    mycursor.execute(sql,idlist)

    readData = mycursor.fetchall()
    breedList = []
    for item in readData:
        breedList.append(item)

    for items in breedList:
        breedObj = m.Breed(items[1],items[2],items[3],items[0])
        breedObj.display()
    
    cnx.close()
    mycursor.close()

def readPupper():
    cnx = connector()
    mycursor = cnx.cursor()
    sql = "SELECT * FROM pupper"
    mycursor.execute(sql)

    readData = mycursor.fetchall()
    breedList = []
    for item in readData:
        breedList.append(item)

    for items in breedList:
        pupperObj = m.Pupper(items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[0])
        pupperObj.display()
    
    cnx.close()
    mycursor.close()

def readBreed():
    cnx = connector()
    mycursor = cnx.cursor()
    sql = "SELECT * FROM breed"
    mycursor.execute(sql)

    readData = mycursor.fetchall()
    breedList = []
    for item in readData:
        breedList.append(item)

    for items in breedList:
        BreedObj = m.Breed(items[1],items[2],items[3],items[0])
        BreedObj.display()
    
    cnx.close()
    mycursor.close()

def readByIdPupper(IDs):
    cnx = connector()
    mycursor = cnx.cursor()
    sql = "SELECT * FROM pupper p join breed b on p.breed_id = b.id where p.id=%s"
    idlist = [str(IDs)]
    mycursor.execute(sql,idlist)

    readData = mycursor.fetchall()
    breedList = []
    for item in readData:
        breedList.append(item)
    
    for items in breedList:
        pupperObj = m.Pupper(items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[0])
        pupperObj.display()
    
    cnx.close()
    mycursor.close()
    

def findPuppersByName(name):
    cnx = connector()
    mycursor = cnx.cursor()
    sql = "SELECT * FROM pupper where name=%s"
    nameList = [name]
    mycursor.execute(sql,nameList)
    
    findName = mycursor.fetchall()
    pupperList = []
    
    for item in findName:
        pupperList.append(item)
    
    for items in pupperList:
        pupperObj = m.Pupper(items[1],items[2],items[3],items[4],items[5],items[6],items[7],items[0])
        pupperObj.display()
    
    cnx.close()
    mycursor.close()

def addPupper(pupperObj):
    cnx = connector()
    mycursor = cnx.cursor()
    try:
        sql = "INSERT INTO pupper (name, sex, weight, height, color, date_of_birth, breed_id) values (%s,%s,%s,%s,%s,%s,%s)"
        newRow = (pupperObj.name, pupperObj.sex, pupperObj.weight, pupperObj.height, pupperObj.color, pupperObj.date_of_birth,pupperObj.breed_id)

        mycursor.execute(sql,newRow)

        if mycursor.lastrowid:
            print('last insert id', mycursor.lastrowid)
        else:
            print('last insert id not found')

        cnx.commit()
    
    finally:
        mycursor.close()
        cnx.close()


def addBreed(breedObj):
    cnx = connector()
    mycursor = cnx.cursor()
    try:
        sql = "INSERT INTO breed (name, temperament, coat) values (%s,%s,%s)"
        newRow = (breedObj.name, breedObj.temperament, breedObj.coat)

        mycursor.execute(sql,newRow)

        if mycursor.lastrowid:
            print('last insert id', mycursor.lastrowid)
        else:
            print('last insert id not found')

        cnx.commit()
    
    finally:
        mycursor.close()
        cnx.close()