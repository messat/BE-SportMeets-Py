from usermodel import selectAllUsers, selectByUsername, addSingleUser, updateSingleUser

def getAllUsers():
    return selectAllUsers()

def getByUsername(username): 
    return selectByUsername(username)

def postSingleUser(newUserData):
    return addSingleUser(newUserData)

def patchSingleUser (updatedUser, username):
    return updateSingleUser(updatedUser, username)
