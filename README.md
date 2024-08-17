## BE-SportMeets

BE-SportMeets is a back-end project for managing sports events, developed using Python, Flask, and PostgreSQL during the final group project at the Northcoders bootcamp. It includes functionalities for user management, event handling and real-time messaging using RESTful API practices.
Here is the front end repo of the app: https://github.com/AFF4NN/FE-SportMeets

## Prerequisites
Python 3
PostgreSQL
pip for Python package management

## Setup
1. Clone the repo
2. Set up a virtual environment: python3 -m venv venv
   source venv/bin/activate
3. Install dependencies: pip install -r requirements.txt
4. Set up the database: psql -f setup.sql
5. Seed the database:
for production: NODE_ENV=production python3 index.py
for development: NODE_ENV=development python3 index.py
6. Start the server: python3 listen.py

Alternatively the endpoints may be tested on software such as Insomnia or Postman.





