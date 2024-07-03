from usermodel import selectAllUsers
from usermodel import selectByUsername
from usermodel import addSingleUser
from usermodel import updateSingleUser

def getAllUsers():
    return selectAllUsers()

def getByUsername(username): 
    return selectByUsername(username)

def postSingleUser(newUserData):
    return addSingleUser(newUserData)

def patchSingleUser (updatedUser, username):
    return updateSingleUser(updatedUser, username)
