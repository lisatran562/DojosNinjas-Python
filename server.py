from flask_app import app
from flask_app.controllers import controller_dojo, controller_ninja
from flask_app.config.mysqlconnection import connectToMySQL


if __name__=="__main__":
    app.run(debug=True)
