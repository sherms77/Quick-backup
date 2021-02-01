# quick backup script
# copies selected folders and pastes them to target drive
# saves log file to target drive

import os, shutil, datetime

def quickBakcup():
    shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/WD HDD 500GB/test_backup1') # erno 13 permission denied error
    # shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/test_backup1') # did not include external drive name to see if it will copy to any usb plugged in
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test') # copies folder and pastes to target
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test')
    stamp = datetime.datetime.now()
    print('Process finished at: ', stamp)

# def log(): # log file function
    
# update to save to external HDD - PermissionError: [Errno 13] Permission denied: '/home/media'
# Next steps:
# 1. need to find out how to allow access.
# https://careerkarma.com/blog/python-permissionerror-errno-13-permission-denied/
# refer to /home/sherms/Python files/csv_import/csv_import.py
# 2. need to change permissions so Python can access external drive - WD HDD 500GB
# 3. after I have finished the program, make executable. elf (executable and linkable format) file in linux.
# Note: refer to /home/Python files/Python permission error for info about file permissions.
# cannot save to an existing folder - need to work out method to create new folder each time or overwrite existing folder.
# possible method to create new folder names for target: use date+time stamp - concatenate to end of folder name
# replicate for each folder to copy
# create log file
# log file needs to print and save the lines of code executed instead of just printing a list of folders copied
# save log file

quickBakcup()

	
