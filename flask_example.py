from flask import Flask

# creat a new Flask instance
app = Flask(__name__)

# the starting point of route, aka root
@app.route('/')
def hello_world():
    return 'Hello World'
