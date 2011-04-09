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
        self.count_titlestmt_subtittle(the_data)
        self.count_frontmatter_subtitle(the_data)
        self.count_titlestmt_author(the_data)
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

    def count_titlestmt_subtittle(self, the_data):
        results = re.findall(r'\<eadheader.*\<titlestmt.*\<subtittle.*\>', the_data)
        if 'titlestmt_subtittle' in self.tag_dict:
            self.tag_dict['titlestmt_subtittle'] = self.tag_dict['titlestmt_subtittle'] + len(results)
        else:
            self.tag_dict['titlestmt_subtittle'] = len(results)

    def count_frontmatter_subtitle(self, the_data):
        results = re.findall(r'\<eadheader.*\<frontmatter.*\<subtittle.*\>', the_data)
        if 'frontmatter_subtitle' in self.tag_dict:
            self.tag_dict['frontmatter_subtitle'] = self.tag_dict['frontmatter_subtitle'] + len(results)
        else:
            self.tag_dict['subtittle'] = len(results)
            
    def count_titlestmt_author(self, the_data):
        results = re.findall(r'\<titlestmt\>.*?\<author.*?\</titlestmt>', the_data, re.DOTALL)
        if 'titlestmt_author' in self.tag_dict:
            self.tag_dict['titlestmt_author'] = self.tag_dict['titlestmt_author'] + len(results)
        else:
            self.tag_dict['titlestmt_author'] = len(results)

if __name__=='__main__':
   main()
