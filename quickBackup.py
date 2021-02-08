import os, shutil, datetime

# 090221: UPTO COPY STAT SECTION IN LINK 3.
# NEXT STEP: Resolve permission error for external drive. Read link 3 in notes doc.
# still Erno 13 error - Permission denied for line 11.

def log(): # log file function
    stamp = datetime.datetime.now()
    print('Process finished at: ', stamp)

def quickBakcup():
    shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/WD HDD 500GB/test_backup1')
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test_hackerrank') # copies locally
    
    log()

quickBakcup()