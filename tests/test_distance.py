'''
Test case for the distance blueprint
'''
import unittest
import json

from app.app import create_app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Creates app before all the tests
        and prepares for the tests
        '''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_address_outside_mkad(self):
        '''
        Checks if the response for a place outside
        MKAD is correct
        '''
        with self.app.app_context():
            param = 'Rio de Janeiro'
            expected_distance = 11558.36
            result = self.client.get(
                '/distance',
                query_string={'address': param}
            )
            status = result.status_code
            result = json.loads(result.data)
            expected = {
                'distance': expected_distance,
                'origin': param
            }
            self.assertEqual(result, expected)
            self.assertEqual(status, 200)

    def test_address_inside_mkad(self):
        '''
        Checks if the response for a place inside
        MKAD is correct
        '''
        with self.app.app_context():
            param = 'Proletarskaya'
            expected_distance = 'Inside MKAD'
            result = self.client.get(
                '/distance',
                query_string={'address': param}
            )
            status = result.status_code
            result = json.loads(result.data)
            expected = {
                'distance': expected_distance,
                'origin': param
            }
            self.assertEqual(result, expected)
            self.assertEqual(status, 200)

    def test_address_in_border(self):
        '''
        Checks if the response for a address
        that is in MKAD border
        '''
        with self.app.app_context():
            param = 'Novogorsk, Moscow Oblast, Russia'
            expected_distance = 'Inside MKAD'
            result = self.client.get(
                '/distance',
                query_string={'address': param}
            )
            status = result.status_code
            result = json.loads(result.data)
            expected = {
                'distance': expected_distance,
                'origin': param
            }
            self.assertEqual(result, expected)
            self.assertEqual(status, 200)

    def test_request_without_address(self):
        '''
        Checks if the response when
        address is not sent is correct
        '''
        with self.app.app_context():
            param = None
            result = self.client.get(
                '/distance',
                query_string={'address': param}
            )
            status = result.status_code
            result = json.loads(result.data)
            expected = {'error': 'Please enter an address'}
            self.assertEqual(result, expected)
            self.assertEqual(status, 400)

    def test_not_found_address(self):
        '''
        Checks if the response for a address
        that doesn't exist is correct
        '''
        with self.app.app_context():
            param = '----'
            result = self.client.get(
                '/distance',
                query_string={'address': param}
            )
            status = result.status_code
            result = json.loads(result.data)
            expected = {'error': 'Address not found'}
            self.assertEqual(result, expected)
            self.assertEqual(status, 404)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
