import shutil, datetime, os
stamp = datetime.datetime.now()

# copies folders
def copy():
    print('\nCopying...')
    exclude = shutil.ignore_patterns('.grsync', 'Public') # folders to exclude
    shutil.copytree('/home/sherms/dir1', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp), ignore=exclude) 
    print('Finished copying.')

copy()
