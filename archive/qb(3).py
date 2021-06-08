import os, shutil, datetime

stamp = datetime.datetime.now()
x = stamp = datetime.datetime.now()

def create_dir():
    directory = str(datetime.datetime.now()) # creates folder with datetime stamp
    parent_dir = '/home/sherms' # parent directory path
    path =os.path.join(parent_dir, directory) # path

    # FLOW OF EXECUTION (ABOVE)
    # 1.create the directory
    # 2.str(datetime.datetime.now()) - current date in
    # 3.'/home/sherms'

    os.mkdir(path)
    print("Directory '% s' created" % directory) # '%' is a string formatting or interpolation operator

create_dir()

'''
def log(): # log file function   
    print('Process finished at: ', stamp)

def quickBackup():
    # shutil.copytree('/home/sherms/HackerRank', '/home/media/sherms/WD HDD 500GB/test_backup1')
    # shutil.copytree('/home/sherms/HackerRank', '/home/sherms/test_hackerrank') # copies locally
    
    # shutil.copytree('/home/sherms/FaN', '/home/sherms/stamp') # 220421: copies to new folder named stamp
    
    shutil.copytree('/home/sherms/FaN', '/home/sherms/stamp') # copies to new folder named stamp

    # log()

quickBackup()
'''