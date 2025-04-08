"""
Gunicorn and WSGI(Web Server Gateway Interface) are both components used in deploying and serving Python web application,
particularly  tho built with web frameworks like Flask and Django.
"""

from app import app, socketio

if __name__ == "__main__":
    socketio.run(app)