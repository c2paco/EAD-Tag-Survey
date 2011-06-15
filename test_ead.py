import random
import unittest

from ead import TagReport

class TestTagRepor(unittest.TestCase):

    def setUp(self):
        self.report = TagReport()

    def test_count_eadid_countrycode_true_positive(self):
        data = """<eadid countrycode="us" encodinganalog="identifier" mainagencycode="mtg"
                  identifier="80444/xv66365"
                  url="http://nwda-db.wsulibs.wsu.edu/findaid/ark:/80444/xv66365">MTGMss505.xml</eadid>"""
        self.report.count_eadid_countrycode(data)
        self.assertEqual(self.report.tag_dict, {'eadid_countrycode': 1})

    def test_count_eadid_countrycode_true_negative(self):
        data = """<eadid encodinganalog="identifier" mainagencycode="mtg"
                  identifier="80444/xv66365"
                  url="http://nwda-db.wsulibs.wsu.edu/findaid/ark:/80444/xv66365">MTGMss505.xml</eadid>"""
        self.report.count_eadid_countrycode(data)
        self.assertEqual(self.report.tag_dict, {'eadid_countrycode': 0})

    def test_count_repository_corpname_true_positive(self):
        data = """<repository label="Repository">
            <corpname>Rare Book, Manuscript, and Special Collections Library, Duke

			 University</corpname>
         </repository>"""
        self.report.count_repository_corpname(data)
        self.assertEqual(self.report.tag_dict, {'repository_corpname': 1})

if __name__ == '__main__':
    unittest.main()
