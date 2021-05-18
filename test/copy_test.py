import os, shutil, datetime

directory = str(datetime.datetime.now()) # creates folder with datetime stamp
parent_dir = '/home/sherms' # parent directory path
path =os.path.join(parent_dir, directory) # path

os.mkdir(path)
print("Directory '% s' created" % directory) # '%' is a string formatting or interpolation operator

# shutil.copytree('/home/sherms/test folder', '/home/sherms/2021-05-14 10:45:26.333585') # error - file exists. has to create new folder each time.
# shutil.copytree('/home/sherms/test folder', '/home/sherms/new')

# shutil.copytree('/home/sherms/test folder', '/home/sherms/%' % directory) # ValueError: incomplete format
shutil.copytree("/home/sherms/test folder", "/home/sherms/'%' " % directory) # ValueError: unsupported format character ''' (0x27) at index 15

# 170521: trying to populate the end of the target path with the folder name generated in the directory variable.
# 170521: I get errors (refer above).

