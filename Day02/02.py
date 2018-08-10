__author__ = "Alien"

import sys,os

print(os.path.dirname(os.path.abspath(__file__)))

sys.path.append('F:\\python-stu\\Day02\\test')
print(sys.path)

from testm import *
a()

