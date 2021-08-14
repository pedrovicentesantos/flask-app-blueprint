import os
from math import cos, sin, asin, sqrt, pi
from dotenv import load_dotenv


def load_config(config_name):
    current_dir = os.getcwd()
    default_config = os.path.join(current_dir, '.env')
    load_dotenv(default_config, override=True)

    if (config_name == 'testing'):
        testing_config = os.path.join(current_dir, '.env_testing')
        load_dotenv(testing_config, override=True)
    else:
        dev_config = os.path.join(current_dir, '.env_dev')
        load_dotenv(dev_config, override=True)


def deg_to_rad(deg):
    if (not isinstance(deg, int) and not isinstance(deg, float)):
        return None
    return deg * (pi / 180)


def haversine(lon1, lat1, lon2, lat2):
    '''
    Calculates the great circle distance between two points
    on the earth (specified in decimal degrees)
    '''
    for value in locals().values():
        if (not isinstance(value, int) and not isinstance(value, float)):
            return None

    radius = 6371  # Radius of earth in kilometers

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
    distance from Moscow Ring Road in log file
    '''
    log_path = os.path.join(os.getcwd(), os.getenv('LOG_PATH'), 'log.log')
    with open(log_path, 'a') as file:
        file.write(f'{address}: {distance}\n')


def is_inside_mkad(distance):
    '''
    From the coordinates found in:
    https://en.wikipedia.org/wiki/Module:Location_map/data/Russia_Moscow_Ring_Road/doc
    we can define a circle with radius 29.05.
    If a point is distant from center by more than 29.05
    then it's outside of MKAD
    Otherwise is inside MKAD
    '''
    MKAD_RADIUS = 29.05
    return distance <= MKAD_RADIUS
