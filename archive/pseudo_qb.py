# pseudo code-quickbackup
import os, shutil, datetime

stamp = datetime.datetime.now()
src_dir = (/home/sherms/dir1) # test dir
included_subdirs = (src1, src2)
dst_dir = ('/home/sherms/{%d%m%y-%H:%M:%S'}.format(stamp))

# shutil.copytree('/home/sherms/source1', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works

# expected output = (/home/sherms/020621-20:02:54) - subs in 020621-20:02:54 is: src1, src2
