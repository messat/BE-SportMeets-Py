from flask import Flask
from usercontroller import getAllUsers  # Import the function correctly
app = Flask(__name__)
from flask import request
from usercontroller import getByUsername
from eventcontroller import getAllEvents
from eventcontroller import getEventByID
from messagecontroller import getMessagesByEventID
from eventcontroller import postSingleEvent

@app.route('/api/sportmeets/users')
def users():
    return getAllUsers()

@app.route('/api/sportmeets/users/<username>')
def user(username):
    return getByUsername(username)

@app.route('/api/sportmeets/events')
def events():
    return getAllEvents()

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

if __name__ == "__main__":
    app.run(debug=True, port=5021)
