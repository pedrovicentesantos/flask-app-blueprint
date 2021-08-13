'''
Test case for the load config function
'''
import unittest
import os

from utils.utils import load_config


class LoadConfigTestCase(unittest.TestCase):
    def test_base_config(self):
        '''
        Checks if base configs are loaded
        '''
        URL = 'https://api.distancematrix.ai/maps/api/geocode/json'
        load_config('testing')
        self.assertEqual(os.getenv('BASE_URL'), URL)

    def test_development_config(self):
        '''
        Checks if development configs are loaded
        '''
        PATH = 'log'
        load_config('development')
        self.assertEqual(os.getenv('LOG_PATH'), PATH)

    def test_testing_config(self):
        '''
        Checks if testing configs are loaded
        '''
        PATH = 'tests'
        load_config('testing')
        self.assertEqual(os.getenv('LOG_PATH'), PATH)

    def test_another_config(self):
        '''
        Checks if development configs are loaded
        for any config name passed
        '''
        PATH = 'log'
        load_config('another')
        self.assertEqual(os.getenv('LOG_PATH'), PATH)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
