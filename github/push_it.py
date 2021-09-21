#!/usr/bin/env python3

'''

    Date: September 21, 2021
'''


import os

commit_message      = input('Commit Comment: ')
working_directory   = 'cd ~/python3'
git_add             = 'git add *'
git_commit          = 'git commit -m "' + commit_message + '"'
git_push            = 'git push origin'

os.system(working_directory)
os.system(git_add)
os.system(git_commit)
os.system(git_push)
