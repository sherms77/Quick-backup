# quick backup script
# copies selected folders and pastes them to target drive
# save log file to target drive

import os, shutil

def quickBackup():
    shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test') # copies folder and pastes to target
    shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test')
    print('Process finished.')

# cannot save to an existing folder - need to work out method to create new folder each time or overwrite existing folder.
# possible method to create new folder names for target: use date+time stamp - concatenate to end of folder name
# update to save to external HDD
# replicate for each folder to copy
# create log file
# log file needs to print and save the lines of code executed instead of just printing a list of folders copied
# save log file

quickBackup()

	
