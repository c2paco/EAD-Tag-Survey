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
        self.parse_eadid_countrycode(filename)
        self.parse_titlestmt_subtittle(filename)
        self.parse_frontmatter_subtitle(filename)
        self.parse_titlestmt_author(filename)

    def display_report(self):
        print "\n==========   Tag Report  ============\n"
        for k, v in self.tag_dict.iteritems():
            print '%s: %s' % (k, v)
        print "\n========   End Tag Report  ==========="
        
             
    
            
    def parse_eadid_countrycode(self, filename):
        f = open(filename, 'r')
        results = re.findall(r'(\<eadid.*countrycode.*\>)', f.read())
        f.close()
        if 'eadid_countrycode' in self.tag_dict:
            self.tag_dict['eadid_countrycode'] = self.tag_dict['eadid_countrycode'] + len(results)
        else:
            self.tag_dict['eadid_countrycode'] = len(results)            

    def parse_titlestmt_subtittle(self, filename):
        f = open(filename, 'r')
        results = re.findall(r'\<eadheader.*\<titlestmt.*\<subtittle.*\>', f.read())
        f.close()
        if 'titlestmt_subtittle' in self.tag_dict:
            self.tag_dict['titlestmt_subtittle'] = self.tag_dict['titlestmt_subtittle'] + len(results)
        else:
            self.tag_dict['titlestmt_subtittle'] = len(results)

    def parse_frontmatter_subtitle(self, filename):
        f = open(filename, 'r')
        results = re.findall(r'\<eadheader.*\<frontmatter.*\<subtittle.*\>', f.read())
        f.close()
        if 'frontmatter_subtitle' in self.tag_dict:
            self.tag_dict['frontmatter_subtitle'] = self.tag_dict['frontmatter_subtitle'] + len(results)
        else:
            self.tag_dict['subtittle'] = len(results)
            
    def parse_titlestmt_author(self, filename):
        f = open(filename, 'r')
        results = re.findall(r'\<eadheader.*\<titlestmt.*\<author.*\</author>', f.read())
        f.close()
        if 'titlestmt_author' in self.tag_dict:
            self.tag_dict['titlestmt_author'] = self.tag_dict['titlestmt_author'] + len(results)
        else:
            self.tag_dict['titlestmt_author'] = len(results)

if __name__=='__main__':
   main()
