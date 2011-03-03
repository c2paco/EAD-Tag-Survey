 
import os
import re
 

f = open('/P0006.xml', 'r')
d (specified below) strings in the object it is reading
results = re.findall(r'\<c02\>|\</c02>', f.read())

print results
