'''
Test case for the haversine function
'''
import unittest

from utils.utils import haversine


class HaversineTestCase(unittest.TestCase):
    def test_distance(self):
        expected = 4523.09206
        location_brazil = [-21.5262653, -61.2703175]
        location_usa = [17.6770471, -72.3477122]
        result = haversine(
            location_brazil[1],
            location_brazil[0],
            location_usa[1],
            location_usa[0]
        )
        self.assertEqual(round(result, 2), round(expected, 2))

    def test_same_point(self):
        expected = 0
        location = [-21.5262653, -61.2703175]
        result = haversine(
            location[1],
            location[0],
            location[1],
            location[0]
        )
        self.assertEqual(round(result, 2), round(expected, 2))

    def test_invalid_param(self):
        expected = None
        location_brazil = [-21.5262653, -61.2703175]
        location_usa = [17.6770471, '-72.3477122']
        result = haversine(
            location_brazil[1],
            location_brazil[0],
            location_usa[1],
            location_usa[0]
        )
        self.assertEqual(result, expected)


if (__name__ == '__main__'):
    unittest.main(verbosity=2)
