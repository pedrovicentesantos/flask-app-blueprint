import os
from math import cos, sin, asin, sqrt, pi

from utils.constants import CURRENT_PATH


def deg_to_rad(deg):
    return deg * (pi / 180)


def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    '''
    radius = 6371  # Radius of earth in kilometers.

    # Convert degrees to radians
    lon1, lat1, lon2, lat2 = map(deg_to_rad, [lon1, lat1, lon2, lat2])

    distance_lon = lon2 - lon1
    distance_lat = lat2 - lat1

    a = sin(distance_lat/2) ** 2 \
        + cos(lat1) * cos(lat2) * sin(distance_lon/2) ** 2

    center = 2 * asin(sqrt(a))

    return center * radius


def save_log(address, distance):
    '''
    Saves the address sent via HTTP request and
    distance from Moscow Ring Road
    '''
    log_path = os.path.join(CURRENT_PATH, 'log', 'log.log')
    with open(log_path, 'a') as file:
        file.write(f'{address}: {distance}\n')
