from model.eventmodel import SelectAllEvents, SelectEventByID, AddEvent, updatingASingleEvent, deleteById, SelectEventByUsername, PostNewUserEvent, SelectEventCategories

def getAllEvents(location, event_category, event_organiser):
    return SelectAllEvents(location, event_category, event_organiser)

def getEventByID(event_id):
    return SelectEventByID(event_id)

def postSingleEvent(newEvent):
    return AddEvent(newEvent)

def patchSingleEvent(updatedEvent, event_id):
    return updatingASingleEvent(updatedEvent, event_id)

def deleteSingleEvent(event_id):
    return deleteById(event_id)

def getEventByUsername(username): 
    return SelectEventByUsername(username)

def sendNewUserEvent(newUserEvent): 
    return PostNewUserEvent(newUserEvent)

def getEventCategories():
    return SelectEventCategories()