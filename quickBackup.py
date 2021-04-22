import os, shutil, datetime
# 220421: WORKING ON STEP 8

stamp = datetime.datetime.now()
x = stamp = datetime.datetime.now()

def log(): # log file function   
    print('Process finished at: ', stamp)

def quickBakcup():
    # shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/WD HDD 500GB/test_backup1')
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test_hackerrank') # copies locally
    
    # shutil.copytree('/home/sherms/FaN', '/home/sherms/stamp') # 220421: copies to new folder named stamp
    
    shutil.copytree('/home/sherms/FaN', '/home/sherms/stamp') # copies to new folder named stamp

    # log()

quickBakcup()