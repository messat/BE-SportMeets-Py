from flask import Flask
from usercontroller import getAllUsers  # Import the function correctly
app = Flask(__name__)
from flask import request
from usercontroller import getByUsername, postSingleUser, patchSingleUser
from eventcontroller import getAllEvents, getEventByID, postSingleEvent, patchSingleEvent, deleteSingleEvent
from messagecontroller import getMessagesByEventID, PostNewMessage


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
    return getAllEvents(location, event_category)

@app.route('/api/sportmeets/events/<event_id>')
def event(event_id):
    return getEventByID(event_id)

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

if __name__ == "__main__":
    app.run(debug=True, port=5022)
