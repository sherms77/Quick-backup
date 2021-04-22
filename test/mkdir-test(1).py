# https://www.geeksforgeeks.org/create-a-directory-in-python/

# syntax: os.mkdir(path, mode=Oo777, *, dir_fd=None)
'''
Paramater:
path = path-like object representing a file system path. Path like object is either a string or bytes object representing a path.
mode (optional) = integer value representing mode of the directory to be created. If this paramater is omitted, the default value Oo777 is used.
dir_fd (optional) = file descriptor referring to a directory. The default value of this paramater is None. If the specified path is absolute then dir_fd is ignored.
'''

'''
220421:
CODE FROM SITE
WILL REPLICATE TO SEE HOW IT WORKS
THEN WILL MODIFY TO TRY AND GET MY DESIRED RESULT
IE: CREATE A NEW DESTINATION FOLDER EACH TIME A COPY IS MADE AND THE DESTINATION FOLDER'S NAME WILL BE THE CURRENT DATE.

# Python program to explain os.mkdir() method
  
# importing os module
import os
  
# Directory
directory = "GeeksforGeeks"
  
# Parent Directory path
parent_dir = "D:/Pycharm projects/"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
  
# Directory
directory = "Geeks"
  
# Parent Directory path
parent_dir = "D:/Pycharm projects"
  
# mode
mode = 0o666
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)
'''
