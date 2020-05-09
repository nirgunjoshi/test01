"""
This script runs the Energy_Sources application using a development server.
"""

from os import environ
from Energy_Source import app
# print(f"this is runserver.py:{__name__}")
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    print(HOST)
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555 
    app.run(HOST, PORT)
