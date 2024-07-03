from messagemodel import SelectAllMessagesByEventID
from messagemodel import AddNewMessage
def getMessagesByEventID(event_id): 
    return SelectAllMessagesByEventID(event_id)

def PostNewMessage(newMessage):
    return AddNewMessage(newMessage)