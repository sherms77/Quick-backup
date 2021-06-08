# copies entire home folder

import shutil, datetime, timeit 

def qb_home(): 
    stamp = datetime.datetime.now()
    print('Copying files...')
    shutil.copytree('/home/sherms/', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works
    print('Process finished: home folder copied to target folder')

# timeit.timeit(stmt, setup, timer, number) accepts four arguments:
setup = "import shutil, datetime"
stmt = """
def qb_home(): 
    stamp = datetime.datetime.now()
    print('Copying files...')
    shutil.copytree('/home/sherms/', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works
    print('Process finished: home folder copied to target folder')
"""

qb_home()
exe_time = timeit.timeit(stmt, setup, number = 1)
print('Execution time: ', exe_time)

# 030621: stopped process at about 6 minutes - it had copied 11/18 folders. 
# Unsure if it completed copies for all files from those folders.
# process takes too long.
