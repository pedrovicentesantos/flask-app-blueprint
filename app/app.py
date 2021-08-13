'''
Creates the Flask app
'''
from flask import Flask, jsonify

from distance.distance import distance_blueprint
from utils.utils import load_config


def create_app(config_name):
    '''
    Uses the config name to load
    the correct configurations for app
    '''
    load_config(config_name)

    app = Flask(__name__)
    # Add the blueprint to the application
    app.register_blueprint(distance_blueprint)

    '''
    Add a handler for when the user
    tries to access a route that doesn't exist
    '''
    @app.errorhandler(404)
    def page_not_found(e):
        response = jsonify({'error': 'Page not found', 'cause': str(e)})
        response.status_code = 404

        return response

    return app


if (__name__ == '__main__'):
    app = create_app('development')
    app.run(debug=True)
