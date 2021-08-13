'''
Test case for the distance blueprint
'''
from logging import setLoggerClass
import unittest
import json

from app.app import create_app


class DistanceBlueprintTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Creates app before all the tests
        and prepares for the tests
        '''
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def test_page_not_found(self):
        '''
        Checks if the response when access to
        a route that doesn't exist is correct
        '''
        with self.app.app_context():
            result = self.client.get('/')
            status = result.status_code
            result = json.loads(result.data)

            expected = 'Page not found'
            self.assertIn(result['error'], expected)
            self.assertEqual(status, 404)

    def test_distance_blueprint_registered(self):
        '''
        Checks if the distance blueprint is
        registered correctly
        '''
        with self.app.app_context():
            for blueprint in self.app.iter_blueprints():
                self.assertEqual(blueprint.name, 'distance_blueprint')


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
