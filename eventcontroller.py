from  eventmodel import SelectAllEvents
from eventmodel import SelectEventByID
from eventmodel import AddEvent
def getAllEvents():
    return SelectAllEvents()
def getEventByID(event_id):
    return SelectEventByID(event_id)
def postSingleEvent(newEvent):
    return AddEvent(newEvent)