from flask import Flask
from apicontroller import getAllUsers  # Import the function correctly
app = Flask(__name__)

@app.route('/api/sportmeets/users')
def users():
    return getAllUsers()

if __name__ == "__main__":
    app.run(debug=True)