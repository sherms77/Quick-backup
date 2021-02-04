import os, shutil, datetime

def quickBakcup():
    shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/WD HDD 500GB/test_backup1') # erno 13 permission denied error
    # shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/test_backup1') # did not include external drive name to see if it will copy to any usb plugged in
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test') # copies folder and pastes to target
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test')
    stamp = datetime.datetime.now()
    print('Process finished at: ', stamp)
# still Erno 13 error - Permission denied.

# def log(): # log file function

quickBakcup()

	
