#!/usr/bin/env python
import shutil
import os
#  os.system("copy foo.txt bar.txt")
#  os.system("rmdel /s /some/folder")
#  os.system("ren blah barf")

shutil.copy('DATA/alice.txt', 'betsy.txt')
shutil.move('betsy.txt', 'betsy_sue.txt')
if os.path.exists('spam'):
    shutil.rmtree('spam')

shutil.make_archive("datafiles", 'zip', 'DATA')
shutil.make_archive("datafiles", 'tar', 'DATA')
shutil.make_archive("datafiles", 'gztar', 'DATA')
shutil.make_archive("datafiles", 'bztar', 'DATA')

print(shutil.disk_usage("."))
