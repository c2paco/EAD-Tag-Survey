import random
import unittest

from ead import TagReport

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.report = TagReport()

    def test_count_eadid_countrycode(self):
        data = """<eadid countrycode="us" encodinganalog="identifier" mainagencycode="mtg"
                  identifier="80444/xv66365"
                  url="http://nwda-db.wsulibs.wsu.edu/findaid/ark:/80444/xv66365">MTGMss505.xml</eadid>"""
        self.report.count_eadid_countrycode(data)
        self.assertEqual(self.report.tag_dict, {'eadid_countrycode': 1})

if __name__ == '__main__':
    unittest.main()
