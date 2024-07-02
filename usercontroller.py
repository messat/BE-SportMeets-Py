from usermodel import selectAllUsers
from usermodel import selectByUsername

def getAllUsers():
    return selectAllUsers()

def getByUsername(username): 
    return selectByUsername(username)