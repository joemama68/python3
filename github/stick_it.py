#!/usr/bin/env python3

'''

    Date: September 21, 2021
'''


import os

version             = '1'
commit_message      = input('Commit Comment: ')
working_directory   = '/home/student/python3'
git_add             = 'git add *'
git_commit          = 'git commit -m "' + commit_message + '"'
git_push            = 'git push origin'

os.chdir(working_directory)
os.system(git_add)
os.system(git_commit)
os.system(git_push)
