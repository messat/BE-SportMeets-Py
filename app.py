from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

from controller.usercontroller import getAllUsers, getByUsername, postSingleUser, patchSingleUser
from controller.eventcontroller import getAllEvents, getEventByID, postSingleEvent, patchSingleEvent, deleteSingleEvent, getEventByUsername, sendNewUserEvent, getEventCategories, getAllUserEvents, getUserEventsByID, getEventLocations
from controller.messagecontroller import getMessagesByEventID, PostNewMessage
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#python pathway 
@app.route('/api/sportmeets/users')
@cross_origin()
def users():
    return getAllUsers()

@app.route('/api/sportmeets/users/<username>')
@cross_origin()
def user(username):
    return getByUsername(username)

@app.route('/api/sportmeets/events')
@cross_origin()
def events():
    location = request.args.get('location')
    event_category = request.args.get('category')
    event_organiser = request.args.get('organiser')
    return getAllEvents(location, event_category, event_organiser)

@app.route('/api/sportmeets/events/<event_id>')
@cross_origin()
def event(event_id):
    return getEventByID(event_id)

@app.route('/api/sportmeets/user-events/<username>')
@cross_origin()
def eventsearch(username):
    return getEventByUsername(username)

@app.route('/api/sportmeets/messages/<event_id>')
@cross_origin()
def messages(event_id):
    return getMessagesByEventID(event_id)

@app.route('/api/sportmeets/events', methods = ['POST'])
@cross_origin()
def post():
    data = request.get_json()
    return postSingleEvent(data)
    

@app.route('/api/sportmeets/events/<event_id>', methods = ['PATCH'])
@cross_origin()
def patch(event_id):
    updatedEvent = request.get_json()
    return patchSingleEvent(updatedEvent, event_id)

@app.route('/api/sportmeets/events/<event_id>', methods = ['DELETE'])
@cross_origin()
def delete(event_id):
    return deleteSingleEvent(event_id)

@app.route('/api/sportmeets/users', methods = ['POST'])
@cross_origin()
def postNewUser():
    newUserData = request.get_json()
    return postSingleUser(newUserData)

@app.route('/api/sportmeets/users/<username>', methods = ['PATCH'])
@cross_origin()
def patchUser(username):
    updatedUser = request.get_json()
    return patchSingleUser (updatedUser, username)

@app.route('/api/sportmeets/messages', methods = ['POST'])
@cross_origin()
def postNewMessage():
    newMessage = request.get_json()
    return PostNewMessage(newMessage)

@app.route('/api/sportmeets/join-event', methods = ['POST'])
@cross_origin()
def postNewUserEvent():
    newUserEvent = request.get_json()
    return sendNewUserEvent(newUserEvent)

@app.route('/api/sportmeets/categories')
@cross_origin()
def categories():
    return getEventCategories()

@app.route('/api/sportmeets/locations')
@cross_origin()
def location():
    return getEventLocations()

@app.route('/api/sportmeets/userevents/<event_id>')
@cross_origin()
def usereventsById(event_id):
    return getUserEventsByID(event_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)