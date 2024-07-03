from  eventmodel import SelectAllEvents
from eventmodel import SelectEventByID
from eventmodel import AddEvent
from eventmodel import updatingASingleEvent
from eventmodel import deleteById


def getAllEvents(location, event_category):
    return SelectAllEvents(location, event_category)

def getEventByID(event_id):
    return SelectEventByID(event_id)

def postSingleEvent(newEvent):
    return AddEvent(newEvent)

def patchSingleEvent(updatedEvent, event_id):
    return updatingASingleEvent(updatedEvent, event_id)

def deleteSingleEvent(event_id):
    return deleteById(event_id)



