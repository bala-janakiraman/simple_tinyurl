from flask import Flask
from app.controller.routes import bp

app = Flask(__name__)
app.secret_key = "dummysecret"

app.register_blueprint(bp)
