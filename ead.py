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
        self.count_unitid_countrycode(the_data)
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
        self.count_publicationstmt_date(the_data)
        self.count_titleproper_date(the_data)
        self.count_creation_date(the_data)
        self.count_titlestmt_subtitle_date(the_data)
        self.count_frontmatter_date(the_data)
        self.count_titleproper_date(the_data)
        self.count_titlepage_subtitle_date(the_data)
        self.record_comments(the_data)
        self.record_eadid_countrycode(the_data)
        self.record_unitid_countrycode(the_data)
        self.record_langcode(the_data)
     
    def create_output_files(self):
        f = open('output/comments.txt', 'w')
        f.write('############## COMMENTS FOUND ####################\n\n')
        f.close()
        
    def create_output_files(self):
        f = open('output/eadid_countrycode.txt', 'w')
        f.write('############## (EADID) COUNTRYCODE(S) FOUND ####################\n\n')
        f.close()

    def create_output_files(self):
        f = open('output/unitid_countrycode.txt', 'w')
        f.write('############## (UNITID) COUNTRYCODE(S) FOUND ####################\n\n')
        f.close() 
        
    def create_output_files(self):
        f = open('output/langcode.txt', 'w')
        f.write('############## LANGCODE(S) FOUND ####################\n\n')
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
        
    def record_eadid_countrycode(self, the_data):
        results = re.findall(r'\<eadid.*?countrycode="(.*?)".*?', the_data, re.DOTALL)
        f = open('output/eadid_countrycode.txt', 'a')
        for item in results:
            f.write(item + '\n\n')
        f.close()    
    
    def record_unitid_countrycode(self, the_data):
        results = re.findall(r'\<unitid.*?countrycode="(.*?)".*?', the_data, re.DOTALL)
        f = open('output/unitid_countrycode.txt', 'a')
        for item in results:
            f.write(item + '\n\n')
        f.close()
        
    def record_langcode(self, the_data):
        results = re.findall(r'\<eadheader.*?langcode="(.*?)".*?', the_data, re.DOTALL)
        f = open('output/langcode.txt', 'a')
        for item in results:
            f.write(item + '\n\n')
        f.close()

    def record_archdesc(self, the_data):
        results = re.findall(r'\<eadheader.*?archdesc="(.*?)".*?', the_data, re.DOTALL)
        f = open('output/archdesc.txt', 'a')
        for item in results:
            f.write(item + '\n\n')
        f.close()

    def count_unitid_countrycode(self, the_data):
        results = re.findall(r'\<unitid.*?countrycode=.*?\</unitid>', the_data, re.DOTALL)
        if 'unitid_countrycode' in self.tag_dict:
            self.tag_dict['unitid_countrycode'] = self.tag_dict['unitid_countrycode'] + len(results)
        else:
            self.tag_dict['unitid_countrycode'] = len(results)            

    def count_eadid_countrycode(self, the_data):
        results = re.findall(r'\<eadid.*?countrycode=.*?\</eadid>', the_data, re.DOTALL)
        if 'unitid_countrycode' in self.tag_dict:
            self.tag_dict['eadid_countrycode'] = self.tag_dict['eadid_countrycode'] + len(results)
        else:
            self.tag_dict['eadid_countrycode'] = len(results)

    def count_titlestmt_subtitle(self, the_data):
        results = re.findall(r'\<eadheader.*?\<titlestmt.*?\<subtitle.*?\>.*?\</eadheader.*?\>', the_data)
        if 'titlestmt_subtitle' in self.tag_dict:
            self.tag_dict['titlestmt_subtitle'] = self.tag_dict['titlestmt_subtitle'] + len(results)
        else:
            self.tag_dict['titlestmt_subtitle'] = len(results)

    def count_titlepage_subtitle(self, the_data):
        results = re.findall(r'\<titlepage.*?\<subtitle.*?\>.*?\</titlepage.*?\>', the_data)
        if 'titlepage_subtitle' in self.tag_dict:
            self.tag_dict['titlepage_subtitle'] = self.tag_dict['titlepage_subtitle'] + len(results)
        else:
            self.tag_dict['titlepage_subtittle'] = len(results)
            
    def count_titlestmt_author(self, the_data):
        results = re.findall(r'\<titlestmt\>.*?\<author.*?\</titlestmt\>', the_data, re.DOTALL)
        if 'titlestmt_author' in self.tag_dict:
            self.tag_dict['titlestmt_author'] = self.tag_dict['titlestmt_author'] + len(results)
        else:
            self.tag_dict['titlestmt_author'] = len(results)

    def count_titlepage_author(self, the_data):
        results = re.findall(r'\<titlepage.*?\<author.*?\>.*?\</titlepage.*?\>', the_data, re.DOTALL)
        if 'titlepage_author' in self.tag_dict:
            self.tag_dict['titlepage_author'] = self.tag_dict['titlepage_author'] + len(results)
        else:
            self.tag_dict['titlepage_author'] = len(results)

    def count_titlepage_sponsor(self, the_data):
        results = re.findall(r'\<titlepage.*?\<sponsor.*?\>.*?\</titlepage.*?\>', the_data, re.DOTALL)
        if 'titlepage_sponsor' in self.tag_dict:
            self.tag_dict['titlepage_sponsor'] = self.tag_dict['titlepage_sponsor'] + len(results)
        else:
            self.tag_dict['titlepage_sponsor'] = len(results)

    def count_titlestmt_titleproper(self, the_data):
        results = re.findall(r'\<eadheader.*?\<titlestmt.*?\<titleproper.*?\>.*?\</eadheader.*?\>', the_data)
        if 'titlestmt_titleproper' in self.tag_dict:
            self.tag_dict['titlestmt_titleproper'] = self.tag_dict['titlestmt_titleproper'] + len(results)
        else:
            self.tag_dict['titlestmt_titleproper'] = len(results)

    def count_titlepage_titleproper(self, the_data):
        results = re.findall(r'\<titlepage.*?\<titleproper.*?\>.*?\</titlepage.*?\>', the_data)
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
        results = re.findall(r'\<titlepage.*?\<publisher.*?\>*?\</titlepage.*?\>', the_data)
        if 'titlepage_publisher' in self.tag_dict:
            self.tag_dict['titlepage_publisher'] = self.tag_dict['titlepage_publisher'] + len(results)
        else:
            self.tag_dict['titlepage_publisher'] = len(results)

    def count_publicationstmt_address(self, the_data):
        results = re.findall(r'\<filedesc\>.*?\<publicationstmt.*?\<address.*?\</filedesc\>', the_data, re.DOTALL)
        if 'publicationstmt_address' in self.tag_dict:
            self.tag_dict['publicationstmt_address'] = self.tag_dict['publicationstmt_address'] + len(results)
        else:
            self.tag_dict['publicationstmt_address'] = len(results)

    def count_repository_address(self, the_data):
        results = re.findall(r'\<did.*?\<repository.*?\<address.*?\>.*?\</did.*?\>', the_data)
        if 'repository_address' in self.tag_dict:
            self.tag_dict['repository_address'] = self.tag_dict['repository_address'] + len(results)
        else:
            self.tag_dict['repository_address'] = len(results)

    def count_publicationstmt_date(self, the_data):
        results = re.findall(r'\<filedesc.*?\<publicationstmt.*?\<date.*?\>.*?\</filedesc.*?\>', the_data)
        if 'publicationstmt_date' in self.tag_dict:
            self.tag_dict['publicationstmt_date'] = self.tag_dict['publicationstmt_date'] + len(results)
        else:
            self.tag_dict['publicationstmt_date'] = len(results)

    def count_titleproper_date(self, the_data):
        results = re.findall(r'\<titlestmt.*?\<titleproper.*?\<date.*?\>.*?\</titlestmt\>', the_data)
        if 'titleproper_date' in self.tag_dict:
            self.tag_dict['titleproper_date'] = self.tag_dict['titleproper_date'] + len(results)
        else:
            self.tag_dict['titleproper_date'] = len(results)

    def count_creation_date(self, the_data):
        results = re.findall(r'\<profiledesc.*?\<creation.*?\<date.*?\>.*?\</profiledesc\>', the_data)
        if 'creation_date' in self.tag_dict:
            self.tag_dict['creation_date'] = self.tag_dict['creation_date'] + len(results)
        else:
            self.tag_dict['creation_date'] = len(results)
            
    def count_titlestmt_subtitle_date(self, the_data):
        results = re.findall(r'\<titlestmt.*?\<subtitle.*?\<date.*?\>.*?\</titlestmt\>', the_data)
        if 'titlestmt_subtitle_date' in self.tag_dict:
            self.tag_dict['titlestmt_subtitle_date'] = self.tag_dict['titlestmt_subtitle_date'] + len(results)
        else:
            self.tag_dict['titlestmt_subtitle_date'] = len(results)

    def count_frontmatter_date(self, the_data):
        results = re.findall(r'\<frontmatter.*?\<titlepage.*?\<date.*?\>.*?\</frontmatter\>', the_data)
        if 'frontmatter_date' in self.tag_dict:
            self.tag_dict['frontmatter_date'] = self.tag_dict['frontmatter_date'] + len(results)
        else:
            self.tag_dict['frontmatter_date'] = len(results)
  
    def count_titleproper_date(self, the_data):
        results = re.findall(r'\<titlepage.*?\<titleproper.*?\<date.*?\>.*?\</titlepage\>', the_data)
        if 'titleproper_date' in self.tag_dict:
            self.tag_dict['titleproper_date'] = self.tag_dict['titleproper_date'] + len(results)
        else:
            self.tag_dict['titleproper_date'] = len(results)  

    def count_titlepage_subtitle_date(self, the_data):
        results = re.findall(r'\<titlepage.*?\<titleproper.*?\<date.*?\>.*?\</titlepage\>', the_data)
        if 'titlepage_subtitle_date' in self.tag_dict:
            self.tag_dict['titlepage_subtitle_date'] = self.tag_dict['titlepage_subtitle_date'] + len(results)
        else:
            self.tag_dict['titlepage_subtitle_date'] = len(results)
            
            
            
if __name__=='__main__':
   main()
