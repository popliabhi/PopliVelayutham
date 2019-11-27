# Dao.py 1
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
        breedObj = m.Breed(items[0],items[1],items[2],items[3])
        breedObj.display()
    
    cnx.close()

def readByIdPupper():
    cnx = connector()
    mycursor = cnx.cursor()
    sql = "SELECT * FROM pupper"
    mycursor.execute(sql)

    readData = mycursor.fetchall()
    breedList = []
    for item in readData:
        breedList.append(item)

    for items in breedList:
        pupperObj = m.Pupper(items[0],items[1],items[2],items[3],items[4],items[5],items[6])
        pupperObj.display()
    
    cnx.close()