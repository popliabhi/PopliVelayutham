#Pupperfinder.py
import controller as c
def showBreedByID():
    searchId = int(input("Enter the id you are looking for: "))
    c.reading(searchId)
    
showBreedByID()  