from flask import request
import json



def configure_routes(app):

    @app.route('/')
    def hello_world():
        return 'Hello, World!'