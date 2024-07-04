from model.messagemodel import SelectAllMessagesByEventID, AddNewMessage

def getMessagesByEventID(event_id): 
    return SelectAllMessagesByEventID(event_id)

def PostNewMessage(newMessage):
    return AddNewMessage(newMessage)