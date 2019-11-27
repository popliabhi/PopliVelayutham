#controller.py
import Dao as d

def readingBreedById(searchById):
    print("Read Breed record:")
    d.readByIdBreed(searchById)

def readingPupperById(searchById):
    print("Read Pupper record:")
    d.readByIdPupper(searchById)
    
def readAllBreeds():
    print("ALL BREEDS: ")
    d.readBreed()
    
def readAllPuppers(): 
    print("ALL PUPPERS: ")
    d.readPupper()
    

def findItem(name):
    print("Find Pupper By name:")
    d.findPuppersByName(name)

def insertPupperItem(pupperObj):
    print("Insert Pupper Record: ")
    d.addPupper(pupperObj)

def insertBreedItem(breedObj):
    print("Insert Breed Record: ")
    d.addBreed(breedObj)
    
    
