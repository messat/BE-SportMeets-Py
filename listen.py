import os
from app import app

# Get the port from environment variables with a default value of 9090
PORT = int(os.environ.get('PORT', 9092))

if __name__ == '__main__':
    # Start the server and log the port
    app.run(host='0.0.0.0', port=PORT, debug=True)
    print(f'Listening on {PORT}...')
