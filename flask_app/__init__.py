from flask import Flask
app = Flask(__name__)

app.secret_key = "SECRET_KEY"

DB = "dojos_and_ninjas_schema"