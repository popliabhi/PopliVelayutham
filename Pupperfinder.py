#Pupperfinder.py
import controller as c
import datetime
import Model as m
from decimal import * 

def actionItems():
    print("Press 1 for Show Breed By ID\n"
          "Press 2 for Show Pupper By ID\n"
          "Press 3 for Show all Breeds\n"
          "Press 4 for Show all Puppers\n"
          "Press 5 for show Pupper By Name\n"
          "Press 6 for insert Pupper\n"
          "Press 7 for insert Breeds\n")
    
    choice = int(input("Your Choice: "))
    
    if choice == 1:
        showBreedByID()
    
    elif choice == 2:
        readingPupperId()
        
    elif choice == 3:
        readAllBreeds()
    
    elif choice == 4:
        readAllPuppers()
    
    elif choice == 5:
        findPupperByName()
    
    elif choice == 6:
        addPupperRecord()
    
    elif choice == 7:
        addBreedRecord()
        
        
        
        
def showBreedByID():
    searchId = int(input("Enter the breed id you are looking for: "))
    c.readingBreedById(searchId)

def readingPupperId():
    searchId = int(input("Enter the pupper id you are looking for: "))
    c.readingPupperById(searchId)

        
def findPupperByName():
    name = input("Enter the pupper name you are looking for: ")
    c.findItem(name)

def addPupperRecord():
    name =input("Enter Puppy Name: ")
    sex = input("Enter Puppy Sex: ")
    weight = Decimal(input("Enter Puppy weight: "))
    height = Decimal(input("Enter Puppy height: "))
    color = input("Enter Puppy Color: ")
    dob = input('Enter a Puppy Date of Birth')
    year, month, day = map(int, dob.split('-'))
    date_of_birth = datetime.date(year, month, day)
    breed_id = int(input('Enter Breed ID: '))
    pupperObj = m.Pupper(name, sex, weight, height, color, date_of_birth, breed_id)
    c.insertPupperItem(pupperObj)

def addBreedRecord():
    name =input("Enter Breed Name: ")
    temperament = input("Enter Temperament: ")
    coat = input("Enter Coat: ")
    breedObj = m.Breed(name,temperament,coat)
    c.insertBreedItem(breedObj)

actionItems()  