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
    assert len(events) == 5

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
def test_get_event_by_id():
    response = app.test_client().get('/api/sportmeets/messages/1')
    messages = json.loads(response.data.decode('utf-8')).get('messages')
    assert type(messages[0]) is dict    
    assert type(messages) is list
    assert messages[0] == {
        'created_at': 'Tue, 02 Jul 2024 11:02:14 GMT', 
        'event_id': 1, 
        'message_body': 'Hi, I would like to join this event', 
        'message_id': 1, 
        'sender': 'DannyBoy'
    }
    assert messages == [
        {'created_at': 'Tue, 02 Jul 2024 11:02:14 GMT',
         'event_id': 1, 
         'message_body': 'Hi, I would like to join this event', 
         'message_id': 1, 
         'sender': 'DannyBoy'
         }, 
         {'created_at': 'Tue, 02 Jul 2024 11:02:14 GMT', 
          'event_id': 1, 
          'message_body': 'Welcome to the world of Social Meets Up!', 
          'message_id': 2,
          'sender': 'Mo'
         }, 
         {'created_at': 'Tue, 02 Jul 2024 11:02:14 GMT', 
          'event_id': 1, 
          'message_body': 'Hey the weather is looking nice!', 
          'message_id': 3, 
          'sender': 'Alex'}
        ]
    
#tests that can post a newEvent  

def test_postNewEvent():
    response = app.test_client().get('/api/sportmeets/messages/1').send()

