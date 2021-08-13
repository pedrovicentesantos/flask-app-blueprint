import requests
from flask import Blueprint, json, jsonify

from utils.utils import haversine, save_log
from utils.constants import API_KEY, BASE_URL, MKAD_LAT, MKAD_LON

distance_blueprint = Blueprint('distance_blueprint', __name__)


@distance_blueprint.route('/distance/<string:address>')
def index(address):
    try:
        if (not address):
            response = jsonify({'error': 'Please enter an addres'})
            response.status_code = 400

            return response

        address = address.strip()

        params = {
            'key': API_KEY,
            'address': address
        }

        api_response = requests.request(
            method='GET',
            url=BASE_URL,
            params=params
        )

        data = json.loads(api_response.text)

        if (not data):
            response = jsonify({'error': 'No return from external API'})
            response.status_code = 400

            return response

        else:
            if (data['status'] == 'ZERO_RESULTS'):
                response = jsonify({'error': 'Address not found'})
                response.status_code = 404

                return response

            if (data['status'] != 'OK'):
                response = jsonify({
                    'error': ('Error during external API call, ',
                              'please try again later'),
                    'cause': data['status']
                })
                response.status_code = 503

                return response

            lat, lon = data['result'][0]['geometry']['location'].values()

            if (lat == 0 or lon == 0):
                response = jsonify({'error': 'Address not found'})
                response.status_code = 404

                return response

            distance = haversine(MKAD_LON, MKAD_LAT, lon, lat)
            distance = round(distance, 2)

            response = jsonify({
                'distance': distance,
                'origin': address
            })
            response.status_code = 200

            save_log(address, distance)

            return response

    except Exception as e:
        response = jsonify({
            'error': 'Error during API call, please try again',
            'cause': str(e)
        })
        response.status_code = 400

        return response
