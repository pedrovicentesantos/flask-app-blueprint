import unittest
import json

from app.app import create_app


class DistanceBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_address_outside_mkad(self):
        with self.app.app_context():
            param = 'Rio de Janeiro'
            expected_distance = 11558.36
            result = self.client.get(f'/distance/{param}')
            status = result.status_code
            result = json.loads(result.data)
            expected = {
                'distance': expected_distance,
                'origin': param
            }
            self.assertEqual(result, expected)
            self.assertEqual(status, 200)

    def test_address_inside_mkad(self):
        with self.app.app_context():
            param = 'Proletarskaya'
            expected_distance = 'Inside MKAD'
            result = self.client.get(f'/distance/{param}')
            status = result.status_code
            result = json.loads(result.data)
            expected = {
                'distance': expected_distance,
                'origin': param
            }
            self.assertEqual(result, expected)
            self.assertEqual(status, 200)

    def test_not_found_address(self):
        with self.app.app_context():
            param = '----'
            result = self.client.get(f'/distance/{param}')
            status = result.status_code
            result = json.loads(result.data)
            expected = {'error': 'Address not found'}
            self.assertEqual(result, expected)
            self.assertEqual(status, 404)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
