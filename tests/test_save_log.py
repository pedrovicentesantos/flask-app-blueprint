'''
Test case for the save log function
'''
from logging import setLogRecordFactory
import unittest
import os

from utils.utils import load_config, save_log


class LoadConfigTestCase(unittest.TestCase):
    def setUp(self):
        '''
        Loads testing config for using
        log inside tests folder and clean
        file content
        '''
        load_config('testing')
        self.log_path = os.path.join(
            os.getcwd(),
            os.getenv('LOG_PATH'),
            'log.log'
        )
        open(self.log_path, 'w').close()

    def test_empty_file(self):
        '''
        Checks if file is empty
        '''
        self.assertEqual(os.path.getsize(self.log_path), 0)

    def test_add_line(self):
        '''
        Checks if line is added correctly
        '''
        save_log('RJ', 15)
        with open(self.log_path, 'r') as file:
            first_line = file.readline()
        expected = 'RJ: 15\n'
        self.assertEqual(first_line, expected)

    def test_add_multiple_lines(self):
        '''
        Checks if multiple lines
        are added correctly
        '''
        save_log('RJ', 15)
        save_log('RJ', 15)
        expected = 'RJ: 15\n'
        with open(self.log_path, 'r') as file:
            lines = file.readlines()
        for line in lines:
            self.assertEqual(line, expected)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
