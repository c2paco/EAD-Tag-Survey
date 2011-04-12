import os
import re
import pprint
import shutil

def main():
    tag_report = TagReport()
    tag_report.delete_and_create_output()
    tag_report.create_output_files()
    dir_name = 'data'
    files_in_dir = os.listdir(dir_name)
    for file in files_in_dir:
        tag_report.parse_file(os.path.join(dir_name, file))
    tag_report.write_and_display_tag_report()

class TagReport(object):

    def __init__(self):
        self.tag_dict = {}
    
    def parse_file(self, filename):
        f = open(filename, 'r')
        the_data = f.read()
        f.close()
        self.count_eadid_countrycode(the_data)
        self.count_titlestmt_subtitle(the_data)
        self.count_titlepage_subtitle(the_data)
        self.count_titlestmt_author(the_data)
        self.count_titlepage_author(the_data)
        self.count_titlepage_sponsor(the_data)
        self.count_titlestmt_titleproper(the_data)
        self.count_titlepage_titleproper(the_data)
        self.count_imprint_publisher(the_data)
        self.count_publicationstmt_publisher(the_data)
        self.count_titlepage_publisher(the_data)
        self.count_publicationstmt_address(the_data)
        self.count_repository_address(the_data)
        self.record_comments(the_data)

    def create_output_files(self):
        f = open('output/comments.txt', 'w')
        f.write('############## COMMENTS FOUND ####################\n\n')
        f.close()

    def delete_and_create_output(self):
        try:
            shutil.rmtree('output')
        except OSError:
            pass
        os.mkdir('output')

    def write_and_display_tag_report(self):
        the_output = self.build_tag_report()
        f = open('output/tag_report.txt', 'w')
        f.write(the_output)
        f.close()
        print the_output

    def build_tag_report(self):
        to_return = ["\n==========   Tag Report  ============\n"]
        for k, v in self.tag_dict.iteritems():
             to_return.append('%s: %s' % (k, v))
        to_return.append("\n========   End Tag Report  ===========\n")
        return '\n'.join(to_return)

    def record_comments(self, the_data):
        results = re.findall(r'\<!--(.*?)--\>', the_data, re.DOTALL)
        f = open('output/comments.txt', 'a')
        for item in results:
            f.write(item + '\n\n')
        f.close()
        
    def count_eadid_countrycode(self, the_data):
        results = re.findall(r'\<eadid.*?countrycode=.*?</eadid>', the_data, re.DOTALL)
        if 'eadid_countrycode' in self.tag_dict:
            self.tag_dict['eadid_countrycode'] = self.tag_dict['eadid_countrycode'] + len(results)
        else:
            self.tag_dict['eadid_countrycode'] = len(results)            

    def count_titlestmt_subtitle(self, the_data):
        results = re.findall(r'\<eadheader.*\<titlestmt.*\<subtitle.*\>', the_data)
        if 'titlestmt_subtitle' in self.tag_dict:
            self.tag_dict['titlestmt_subtitle'] = self.tag_dict['titlestmt_subtitle'] + len(results)
        else:
            self.tag_dict['titlestmt_subtitle'] = len(results)

    def count_titlepage_subtitle(self, the_data):
        results = re.findall(r'\<frontmatter.*\<titlepage*\<subtitle.*\>', the_data)
        if 'titlepage_subtitle' in self.tag_dict:
            self.tag_dict['titlepage_subtitle'] = self.tag_dict['titlepage_subtitle'] + len(results)
        else:
            self.tag_dict['titlepage_subtittle'] = len(results)
            
    def count_titlestmt_author(self, the_data):
        results = re.findall(r'\<titlestmt\>.*?\<author.*?\</titlestmt>', the_data, re.DOTALL)
        if 'titlestmt_author' in self.tag_dict:
            self.tag_dict['titlestmt_author'] = self.tag_dict['titlestmt_author'] + len(results)
        else:
            self.tag_dict['titlestmt_author'] = len(results)

    def count_titlepage_author(self, the_data):
        results = re.findall(r'\<frontmatter.*\<titlepage.*\<author.*\>', the_data, re.DOTALL)
        if 'titlepage_author' in self.tag_dict:
            self.tag_dict['titlepage_author'] = self.tag_dict['titlepage_author'] + len(results)
        else:
            self.tag_dict['titlepage_author'] = len(results)

    def count_titlepage_sponsor(self, the_data):
        results = re.findall(r'\<frontmatter.*\<titlepage.*\<sponsor.*\>', the_data, re.DOTALL)
        if 'titlepage_sponsor' in self.tag_dict:
            self.tag_dict['titlepage_sponsor'] = self.tag_dict['titlepage_sponsor'] + len(results)
        else:
            self.tag_dict['titlepage_sponsor'] = len(results)

    def count_titlestmt_titleproper(self, the_data):
        results = re.findall(r'\<eadheader.*\<titlestmt.*\<titleproper.*\>', the_data)
        if 'titlestmt_titleproper' in self.tag_dict:
            self.tag_dict['titlestmt_titleproper'] = self.tag_dict['titlestmt_titleproper'] + len(results)
        else:
            self.tag_dict['titlestmt_titleproper'] = len(results)

    def count_titlepage_titleproper(self, the_data):
        results = re.findall(r'\<frontmatter.*\<titlepage*\<titleproper.*\>', the_data)
        if 'titlepage_titleproper' in self.tag_dict:
            self.tag_dict['titlepage_titleproper'] = self.tag_dict['titlepage_titleproper'] + len(results)
        else:
            self.tag_dict['titlepage_titleproper'] = len(results)

    def count_imprint_publisher(self, the_data):
        results = re.findall(r'\<bibliography.*\<imprint.*\<publisher.*\>', the_data, re.DOTALL)
        if 'imprint_publisher' in self.tag_dict:
            self.tag_dict['imprint_publisher'] = self.tag_dict['imprint_publisher'] + len(results)
        else:
            self.tag_dict['imprint_publisher'] = len(results)

    def count_publicationstmt_publisher(self, the_data):
        results = re.findall(r'\<filedesc\>.*?\<publicationstmt.*?\<publisher.*?\</filedesc>', the_data, re.DOTALL)
        if 'publicationstmt_publisher' in self.tag_dict:
            self.tag_dict['publicationstmt_publisher'] = self.tag_dict['publicationstmt_publisher'] + len(results)
        else:
            self.tag_dict['publicationstmt_publisher'] = len(results)

    def count_titlepage_publisher(self, the_data):
        results = re.findall(r'\<frontmatter.*\<titlepage*\<publisher.*\>', the_data)
        if 'titlepage_publisher' in self.tag_dict:
            self.tag_dict['titlepage_publisher'] = self.tag_dict['titlepage_publisher'] + len(results)
        else:
            self.tag_dict['titlepage_publisher'] = len(results)

    def count_publicationstmt_address(self, the_data):
        results = re.findall(r'\<filedesc\>.*?\<publicationstmt.*?\<address.*?\</filedesc>', the_data, re.DOTALL)
        if 'publicationstmt_address' in self.tag_dict:
            self.tag_dict['publicationstmt_address'] = self.tag_dict['publicationstmt_address'] + len(results)
        else:
            self.tag_dict['publicationstmt_address'] = len(results)

    def count_repository_address(self, the_data):
        results = re.findall(r'\<did.*\<repository*\<address.*\>', the_data)
        if 'repository_address' in self.tag_dict:
            self.tag_dict['repository_address'] = self.tag_dict['repository_address'] + len(results)
        else:
            self.tag_dict['repository_address'] = len(results)



if __name__=='__main__':
   main()
