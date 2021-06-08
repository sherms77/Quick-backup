import shutil, datetime, os

stamp = datetime.datetime.now()

# list files and directories
def dir_list():
    srcdir = os.listdir('/home/sherms/dir1')
    print('Directory contents: ')
    for i in zip(srcdir):
        print(i)

dir_list()

# copytree syntax & paramaters - shutil.copytree(src, dst, symlinks, ignore)
print('\nCopying files...')
# shutil.copytree('/home/sherms/dir1', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp), symlinks = False, ignore=shutil.ignore_patterns('ignore1', 'src1')) # this works

# folders = input('ignore1', 'src1') # folders to exclude - trying to work out a way to store folder names in a variable and use a single variable in ignore_patterns argument. This can let me print the folders that were excluded instead of manually typing them out.
# I might not worry about this (abnove line) bc I need to finish this project. Been working on it for 6 months.

exclude = shutil.ignore_patterns('ignore1', 'src1') # folders to exclude
shutil.copytree('/home/sherms/dir1', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp), ignore=exclude) # this works
print('Finished copying files.')
print("""Folders copied:
         - src2
         - t&cs.docx""")
