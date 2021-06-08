import datetime, os, shutil

# python docs - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# dd (day) - %d
# mm (month) - %m
# yy (year) - %y
# hh (hour) - %H
# mm (minute) - %M
# ss (seconds) - %S

stamp = datetime.datetime.now()

# path = 'test path using str formatting: /home/sherms/{0}'.format(stamp)
# testPath = 'test path using str formatting: /home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)

# print(path) # works
# print(testPath)

# format timedate to: dd-mm-yy hh:mm:ss - 240521: formatted timedate - refer to testPath var.
# 260521: need to copy folder to new folder with time date stamp

# shutil.copytree('/home/sherms/test folder', '/home/sherms/test1') # works

# shutil.copytree('/home/sherms/test folder', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works

# test - two different folders to same target folder
print('Copying files...')
shutil.copytree('/home/sherms/source1', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works
# shutil.copytree('/home/sherms/source2', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works
print('Files copied.')

# 270521: test did not work. only copied one folder, source1 to target. could not copy source2 bc target folder already exists.
# 270521: need to work out way to copy multiple folders to the same target folder.

# test 2 - copy whole home folder to target folder
# print('Copying files...')
# shutil.copytree('/home/sherms', '/home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)) # works
# print('Process finished: home folder copied to target folder')

# 270521: Process to copy entire home folder takes a while. I killed it at 3 minutes.
# 270521: Rethink this.
