from flask import Flask, jsonify

from distance.distance import distance_blueprint
from utils.utils import load_config


def create_app(config_name):
    load_config(config_name)

    app = Flask(__name__)
    app.register_blueprint(distance_blueprint)

    @app.errorhandler(404)
    def page_not_found(e):
        print(e)
        response = jsonify({'error': 'Page not found', 'cause': str(e)})
        response.status_code = 404

        return response

    return app


if (__name__ == '__main__'):
    app = create_app('development')
    app.run(debug=True)
