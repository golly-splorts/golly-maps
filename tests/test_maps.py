import subprocess
import os
import unittest
from golly_maps.maps import (
    get_patterns,
    get_map,
    get_map_data,
    get_pattern_by_name
)


HERE = os.path.split(os.path.abspath(__file__))[0]

PATTERNS = [
    "eightpi",
    "eightr",
    "fourrabbits",
    "quadjustyna",
    "random",
    "randompartition",
    "spaceshipcluster",
    "spaceshipcrash",
    "timebomb",
    "twoacorn",
    "twomultum",
    "twospaceshipgenerators",
]


class MapsTest(unittest.TestCase):
    """
    Test maps functionality in the golly maps package.
    """
    def test_get_patterns(self):
        patterns = get_patterns()
        for pattern_name in PATTERNS:
            self.assertIn(pattern_name, patterns)

    def test_get_map(self):
        for pattern_name in PATTERNS:
            r = 100
            c = 120
            m = get_map(pattern_name, rows=r, cols=c)
            req_keys = [
                'patternName',
                'mapName',
                'url',
                'rows',
                'columns',
                'cellSize',
                'initialConditions1',
                'initialConditions2',
                'mapZone1Name',
                'mapZone2Name',
                'mapZone3Name',
                'mapZone4Name'
            ]
            for rk in req_keys:
                self.assertIn(rk, m.keys())

    def test_get_map_data(self):
        for pattern_name in PATTERNS:
            dat = get_map_data(pattern_name)
            req_keys = [
                'patternName',
                'mapName',
                'mapZone1Name',
                'mapZone2Name',
                'mapZone3Name',
                'mapZone4Name'
            ]
            for rk in req_keys:
                self.assertIn(rk, dat.keys())

