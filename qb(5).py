# README file in quickbackup folder has docs
import shutil, datetime, os
stamp = datetime.datetime.now() # creates target folder - uses datetime.now() as name

# list files and directories
def dir_list():
    srcdir = os.listdir('/home/sherms')
    print('Directory contents - including hidden: ')
    for i in zip(srcdir):
        print(i)

# copies folders
def copy():
    print('\nCopying...')
    exclude = shutil.ignore_patterns('.grsync', 'Public', '.gnupg', '.mozilla', '.pylint.d', 'Downloads', 'snap', '.cache', 'Desktop', '.pki', '.gnome', '.local', 'Music', '.idlerc', '.dbus', '.ssh', 'Videos', '.vscode', '.config') # folders to exclude
    shutil.copytree('/home/sherms', '/home/sherms/{:%d%m%y_%H-%M-%S}'.format(stamp), ignore=exclude)
    print('Finished copying.')
    
# prints excluded folders
def excluded():
    e = ['.grsync', 'Public', '.gnupg', '.mozilla', '.pylint.d', 'Downloads', 'snap', '.cache', 'Desktop', '.pki', '.gnome', '.local', 'Music', '.idlerc', '.dbus', '.ssh', 'Videos', '.vscode', '.config'] # list of copied folders
    print('\nExcluded folders - including hidden: ')
    for j in e:
        print(j)

dir_list()
copy()
excluded()
