# code only
# 220421: replicating example

'''
syntax: os.mkdir(path, mode=Oo777, *, dir_fd=None)

Paramater:
path = path-like object representing a file system path. Path like object is either a string or bytes object representing a path.
mode (optional) = integer value representing mode of the directory to be created. If this paramater is omitted, the default value Oo777 is used.
dir_fd (optional) = file descriptor referring to a directory. The default value of this paramater is None. If the specified path is absolute then dir_fd is ignored.
'''

import os, datetime 

# directory
directory = datetime.datetime.now()

# parent directory path
# 220421: UP TO HERE
# parent_dir = 
