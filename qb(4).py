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
shutil.copytree('/home/sherms/dir1', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp), symlinks = False, ignore=shutil.ignore_patterns('/home/sherms/dir1/ignore1')) # it did not exclude the ignore1 folder
