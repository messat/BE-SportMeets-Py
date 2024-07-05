import pytest
import json
from app import app

# commands to use in terminal to run the tests 
# pytest -rP ./tests/test_project.py
# pytest -rx ./tests/test_project.py

#tests that retrieves all the users

def test_get_all_users():
    response = app.test_client().get('/api/sportmeets/users')
    users = json.loads(response.data.decode('utf-8')).get('users')
    assert type(users[0]) is dict
    assert users[0]["name"] == "Muhammad"
    assert response.status_code == 200
    assert type(users) is list
    assert len(users) == 3

#tests that retrieves a specified user
def test_get_a_user():
    response = app.test_client().get('/api/sportmeets/users/Mo')
    user = json.loads(response.data.decode('utf-8')).get('user')
    assert type(user[0]) is dict
    assert user[0]["name"] == "Muhammad"
    assert response.status_code == 200
    assert type(user) is list

#tests that retrieves all events 
def test_get_all_events():
    response = app.test_client().get('/api/sportmeets/events')
    events = json.loads(response.data.decode('utf-8')).get('events')
    assert type(events[0]) is dict    
    assert events[0] == {
        'created_at': 'Fri, 19 Jul 2024 10:23:54 GMT', 
        'event_category': 'football', 
        'event_description': 'Playing football with Northcoders Colleagues', 
        'event_id': 1, 
        'event_img_url': 'https://cdn.pixabay.com/photo/2016/05/27/14/33/football-1419954_640.jpg', 
        'event_location': 'Leeds', 
        'event_name': 'Soccer Star Solutions', 
        'event_organiser': 'Alex', 
        'event_spaces_available': 20}
    assert events[2] == {
        'created_at': 'Wed, 24 Jul 2024 15:10:30 GMT', 
        'event_category': 'Golf', 
        'event_description': 'Playing Golf with Big Boys', 
        'event_id': 3, 
        'event_img_url': 'https://cdn.shopify.com/s/files/1/0576/2750/8872/files/Golf_Birdie_480x480.jpg?v=1676301047', 
        'event_location': 'Manchester', 
        'event_name': 'Birdie Bound', 
        'event_organiser': 'Mo', 
        'event_spaces_available': 5
    }
    assert response.status_code == 200
    assert type(events) is list

#tests that retrieve an event by event ID 
def test_get_event_by_id():
    response = app.test_client().get('/api/sportmeets/events/1')
    event = json.loads(response.data.decode('utf-8')).get('event')
    assert type(event[0]) is dict    
    assert type(event) is list
    assert event[0] == {
        'created_at': 'Fri, 19 Jul 2024 10:23:54 GMT', 
        'event_category': 'football', 
        'event_description': 'Playing football with Northcoders Colleagues', 
        'event_id': 1, 
        'event_img_url': 'https://cdn.pixabay.com/photo/2016/05/27/14/33/football-1419954_640.jpg', 
        'event_location': 'Leeds', 
        'event_name': 'Soccer Star Solutions', 
        'event_organiser': 'Alex', 
        'event_spaces_available': 20
    }

#tests that retrieve all messages for an event by event ID 
def test_get_messages_by_id():
    response = app.test_client().get('/api/sportmeets/messages/1')
    messages = json.loads(response.data.decode('utf-8')).get('messages')
    assert type(messages[0]) is dict    
    assert type(messages) is list
    assert messages[1]["event_id"] == 1   
    assert messages[1]["message_body"] == 'Welcome to the world of Social Meets Up!'
    assert messages[1]["message_id"] == 2
    assert messages[1]["sender"] == "Mo" 
    
#tests that can post a newEvent  
def test_postNewEvent():
    created_at = "Fri, 19 Jul 2024 10:23:54 GMT"
    event_category = "pool"
    event_description = "Playing pool in cuzzy garage"
    event_img_url = "https://nwscdn.com/media/catalog/product/cache/all/thumbnail/800x/0dc2d03fe217f8c83829496872af24a0/p/o/pool-table.jpg"
    event_location = "Manchester"
    event_name = "Return of Ronnie O Sullivan"
    event_organiser = "Mo"
    event_spaces_available = 35 
    eventData = {"created_at": created_at,"event_category": event_category, "event_description": event_description,"event_img_url": event_img_url, "event_location": event_location,"event_name": event_name, "event_organiser": event_organiser, "event_spaces_available": event_spaces_available }
    response = app.test_client().post('/api/sportmeets/events', json =eventData)
    newEvent = json.loads(response.data.decode('utf-8')).get('PostedEvent')
    assert response.status_code == 200
    assert newEvent["event_category"] == "pool"
    assert type(newEvent["event_id"]) == int
    assert newEvent["event_name"] == "Return of Ronnie O Sullivan"
    assert newEvent["event_organiser"] == "Mo"
    assert newEvent["event_spaces_available"] == 35
    assert newEvent["event_location"] == "Manchester"
 
def test_updateEventById():
    created_at = "2024-07-24 16:45:20"
    event_category = "basketball"
    event_description = "Playing Basketball at the wembley stadium"
    event_img_url = "https://lh3.googleusercontent.com/AF1QipOAGnbz5S8g1OF41CdH_jN1vBxD8TNR5ehV3CVy=s1360-w1360-h1020"
    event_location =  "London"
    event_name = "Bounce Ballers"
    event_organiser = "DannyBoy"
    event_spaces_available = 20
    eventData = {
        "created_at": created_at,
        "event_category": event_category, 
        "event_description": event_description, 
        "event_img_url": event_img_url, 
        "event_location": event_location,
        "event_name": event_name, 
        "event_organiser": event_organiser, 
        "event_spaces_available": event_spaces_available 
    }
    response = app.test_client().patch('/api/sportmeets/events/2', json =eventData)
    updatingAnEvent = json.loads(response.data.decode('utf-8')).get('UpdatedEvent')
    assert updatingAnEvent["event_description"] == "Playing Basketball at the wembley stadium"
    assert updatingAnEvent["event_location"] == "London"
    assert updatingAnEvent["event_spaces_available"] == 20
    
def test_deleteByID():
    response = app.test_client().delete('/api/sportmeets/events/4')
    deleteAnEvent = json.loads(response.data.decode('utf-8'))


def test_postNewUser():
    username = "Alex_G"
    name = "Alexander Greaves"
    password = "Linux"
    avatar_url = "https://www.stepex.co/wp-content/uploads/2022/04/stepex-northcoders-1.jpg"

    userData = { 
        "username": username,
        "name": name, 
        "password": password,
        "avatar_url": avatar_url
    }
    response = app.test_client().post('/api/sportmeets/users', json =userData)
    postedUser = json.loads(response.data.decode('utf-8')).get('newUser')
    assert postedUser["username"] == "Alex_G"
    assert postedUser["name"] == "Alexander Greaves"
    assert postedUser["password"] == "Linux"
    assert postedUser["avatar_url"] == "https://www.stepex.co/wp-content/uploads/2022/04/stepex-northcoders-1.jpg"


def test_updateUserDetailsByUsername():
    name = "Affan Mohammed"
    password = "I love spanish"
    avatar_url = "https://media.istockphoto.com/id/1488582613/vector/espanol.jpg?s=612x612&w=0&k=20&c=YNtI5mRozRDAJ_X-rp_1ABHPozceKPjxwRPa1HOvZNA="
    userData = {
        "name": name, 
        "password": password, 
        "avatar_url": avatar_url
    }
    response = app.test_client().patch('/api/sportmeets/users/Alex', json =userData)
    updatingUser = json.loads(response.data.decode('utf-8')).get('UpdatedUser')
    assert updatingUser["name"] == "Affan Mohammed"
    assert updatingUser["password"] == "I love spanish"
    assert updatingUser["avatar_url"] == "https://media.istockphoto.com/id/1488582613/vector/espanol.jpg?s=612x612&w=0&k=20&c=YNtI5mRozRDAJ_X-rp_1ABHPozceKPjxwRPa1HOvZNA="

def test_postNewMessage():
    newMessage = {
    "message_body": "This is a brand new posted message",
    "sender": "DannyBoy",
    "event_id": 1
    }
    response = app.test_client().post('/api/sportmeets/messages', json =newMessage)
    postedMessage = json.loads(response.data.decode('utf-8')).get('PostedMessage')
    assert postedMessage["message_body"] == "This is a brand new posted message"
    assert postedMessage["sender"] == "DannyBoy"
    assert postedMessage["event_id"] == 1

def test_filterByLocation():
    response = app.test_client().get('/api/sportmeets/events?location=Manchester')
    eventsByLocation = json.loads(response.data.decode('utf-8')).get('events')
    assert len(eventsByLocation) == 1

def test_filterBySport():
    response = app.test_client().get('/api/sportmeets/events?category=football')
    eventsByCategory = json.loads(response.data.decode('utf-8')).get('events')
    assert len(eventsByCategory) == 1

def test_filterByLocationAndSport():
    response = app.test_client().get('/api/sportmeets/events?location=Leeds&category=football')
    filteredByLocationAndCategory = json.loads(response.data.decode('utf-8')).get('events')
    assert len(filteredByLocationAndCategory) == 1


def test_filterEventsByEventOrganiser():
    response = app.test_client().get('/api/sportmeets/events?organiser=DannyBoy')
    filteredByEventOrganiser = json.loads(response.data.decode('utf-8')).get('events')
    assert filteredByEventOrganiser[0]["event_category"] == "basketball"
    assert filteredByEventOrganiser[0]["event_organiser"] == "DannyBoy"
    assert filteredByEventOrganiser[0]["event_img_url"] == "https://storage.googleapis.com/pod_public/1300/180358.jpg"

def test_getAllEventsForUser():
    response = app.test_client().get('/api/sportmeets/user-events/Mo')
    userEventsArr = json.loads(response.data.decode('utf-8')).get('UserEvents')
    assert userEventsArr[0]["event_id"] == 1

def test_postUserEvent():
    userevent = { "username": "Mo",
                  "event_id": 2}
    response = app.test_client().post('/api/sportmeets/join-event', json =userevent)
    userEvent = json.loads(response.data.decode('utf-8')).get('PostedUserEvent')
    assert response.status_code == 200
    assert userEvent["event_id"] == 2
    assert userEvent["username"] == "Mo"

def test_getSportCategories(): 
    response = app.test_client().get('/api/sportmeets/categories')
    userEvent = json.loads(response.data.decode('utf-8')).get('Event_Categories')
    assert len(userEvent) == 3    
