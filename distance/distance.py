'''
Defines the distance Blueprint
with the route /distance/{address}
that returns the distance from a place to
MKAD in kilometers
'''

import requests
import os
from flask import Blueprint, json, jsonify, request

from utils.utils import haversine, save_log, is_inside_mkad

distance_blueprint = Blueprint('distance_blueprint', __name__)


@distance_blueprint.route('/distance')
def index():
    try:
        # Gets the address sent via HTTP request
        address = request.args.get('address')
        if (not address):
            response = jsonify({'error': 'Please enter an address'})
            response.status_code = 400

            return response

        address = address.strip()

        params = {
            'key': os.getenv('API_KEY'),
            'address': address
        }
        '''
        Use an external API to obtain
        coordinates of the address
        '''
        api_response = requests.request(
            method='GET',
            url=os.getenv('BASE_URL'),
            params=params
        )

        data = json.loads(api_response.text)

        if (not data):
            response = jsonify({'error': 'No return from external API'})
            response.status_code = 400

            return response

        else:
            # The external API returns ZERO_RESULTS if address is not found
            if (data['status'] == 'ZERO_RESULTS'):
                response = jsonify({'error': 'Address not found'})
                response.status_code = 404

                return response

            '''
            Other types of errors have status different
            from OK and ZERO_RESULTS
            '''
            if (data['status'] != 'OK'):
                response = jsonify({
                    'error': ('Error during external API call, ',
                              'please try again later'),
                    'cause': data['status']
                })
                response.status_code = 503

                return response
            # Gets the latitude and longitude returned from the API
            lat, lon = data['result'][0]['geometry']['location'].values()

            '''
            The API can also return latitude and longitude
            as 0 if address is not found
            '''
            if (lat == 0 and lon == 0):
                response = jsonify({'error': 'Address not found'})
                response.status_code = 404

                return response

            '''
            Calcutes the distance between the address and the MKAD
            using the haversine formula
            '''
            distance = haversine(
                float(os.getenv('MKAD_LON')),
                float(os.getenv('MKAD_LAT')),
                lon,
                lat
            )

            '''
            Checks if the point is inside MKAD
            and adapts the response
            '''
            if (is_inside_mkad(distance)):
                distance = 'Inside MKAD'
            else:
                distance = round(distance, 2)

            response = jsonify({
                'distance': distance,
                'origin': address
            })
            response.status_code = 200

            # Saves in the log address and distance
            save_log(address, distance)

            return response

    except Exception as e:
        '''
        Catch exceptions and returns it
        '''
        response = jsonify({
            'error': 'Error during API call, please try again',
            'cause': str(e)
        })
        response.status_code = 400

        return response
