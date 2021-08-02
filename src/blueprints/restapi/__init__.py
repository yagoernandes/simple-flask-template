from src.blueprints.restapi.hello_world import HelloWorld
from flask import Blueprint
from flask_restful import Api

bp = Blueprint('restapi', __name__, url_prefix='/api/v1')
api = Api(bp)

def init_app(app):
	api.add_resource(HelloWorld, '/')
	app.register_blueprint(bp)