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
directory = str(datetime.datetime.now()) # creates new folder with datetime stamp

# parent directory path
parent_dir = '/home/sherms'

# path
path =os.path.join(parent_dir, directory)

# create the directory
# date.today() - current date in
# '/home/sherms'
os.mkdir(path)
print("Directory '% s' created" % directory)

# 060521: Fixed join() argument must be str error.
# 060521: Did not code out the rest of the example.
# 060521: Got to work as required. Creates new folder named with date time stamp everytime.

'''
230421: UP TO HERE. 
UNSURE IF I WILL CODE THIS OUT AS THIS IS ANTOHER EXAMPLE USING THE OPTIONAL MODE PARAMATER.
WILL RUN ABOVE CODE FIRST TO SEE HOW IT WORKS.
# directory
directory = ''
'''
