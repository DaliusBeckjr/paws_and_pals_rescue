from flask_app import app 
from flask_app.controllers import users, rescues







if __name__ == '__main__':
    app.run(debug = True, port = 8000)