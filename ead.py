import os
import re
import pprint

def main():
    tag_report = TagReport()
    dir_name = 'data'
    files_in_dir = os.listdir(dir_name)
    for file in files_in_dir:
        tag_report.parse_file(os.path.join(dir_name, file))
    tag_report.display_report()

class TagReport(object):

    def __init__(self):
        self.tag_dict = {}

    def parse_file(self, filename):
        self.parse_c02(filename)

    def display_report(self):
        print "\n==========   Tag Report  ============\n"
        for k, v in self.tag_dict.iteritems():
            print '%s: %s' % (k, v)
        print "\n========   End Tag Report  ==========="
        print "\n\n\n\n\n\nLongCat is l%sng" % ''.join(['o' for r in range(1000)])

    def parse_c02(self, filename):
        f = open(filename, 'r')
        results = re.findall(r'\<c02\>|\</c02>', f.read())
        f.close()
        if 'c02' in self.tag_dict:
            self.tag_dict['c02'] = tag_dict['c02'] + len(results)
        else:
            self.tag_dict['c02'] = len(results)

if __name__=='__main__':
   main()
