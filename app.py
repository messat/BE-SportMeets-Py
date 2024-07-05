from flask import Flask
from flask import request

from controller.usercontroller import getAllUsers, getByUsername, postSingleUser, patchSingleUser
from controller.eventcontroller import getAllEvents, getEventByID, postSingleEvent, patchSingleEvent, deleteSingleEvent, getEventByUsername, sendNewUserEvent, getEventCategories
from controller.messagecontroller import getMessagesByEventID, PostNewMessage
app = Flask(__name__)

@app.route('/api/sportmeets/users')
def users():
    return getAllUsers()

@app.route('/api/sportmeets/users/<username>')
def user(username):
    return getByUsername(username)

@app.route('/api/sportmeets/events')
def events():
    location = request.args.get('location')
    event_category = request.args.get('category')
    event_organiser = request.args.get('organiser')
    return getAllEvents(location, event_category, event_organiser)

@app.route('/api/sportmeets/events/<event_id>')
def event(event_id):
    return getEventByID(event_id)

@app.route('/api/sportmeets/user-events/<username>')
def eventsearch(username):
    return getEventByUsername(username)

@app.route('/api/sportmeets/messages/<event_id>')
def messages(event_id):
    return getMessagesByEventID(event_id)


@app.route('/api/sportmeets/events', methods = ['POST'])
def post():
    data = request.get_json()
    return postSingleEvent(data)

@app.route('/api/sportmeets/events/<event_id>', methods = ['PATCH'])
def patch(event_id):
    updatedEvent = request.get_json()
    return patchSingleEvent(updatedEvent, event_id)

@app.route('/api/sportmeets/events/<event_id>', methods = ['DELETE'])
def delete(event_id):
    return deleteSingleEvent(event_id)

@app.route('/api/sportmeets/users', methods = ['POST'])
def postNewUser():
    newUserData = request.get_json()
    return postSingleUser(newUserData)

@app.route('/api/sportmeets/users/<username>', methods = ['PATCH'])
def patchUser(username):
    updatedUser = request.get_json()
    return patchSingleUser (updatedUser, username)

@app.route('/api/sportmeets/messages', methods = ['POST'])
def postNewMessage():
    newMessage = request.get_json()
    return PostNewMessage(newMessage)

@app.route('/api/sportmeets/join-event', methods = ['POST'])
def postNewUserEvent():
    newUserEvent = request.get_json()
    return sendNewUserEvent(newUserEvent)

@app.route('/api/sportmeets/categories')
def categories():
    return getEventCategories()

# if __name__ == "__main__":
#     app.run(debug=True, port=5022)
