from flask import Flask
import src.blueprints.restapi as restapi

app = Flask(__name__)

restapi.init_app(app)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"