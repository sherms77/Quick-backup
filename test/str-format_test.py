import datetime
# python docs - https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

# dd (day) - %d
# mm (month) - %m
# yy (year) - %y
# hh (hour) - %H
# mm (minute) - %M
# ss (seconds) - %S

stamp = datetime.datetime.now()
path = 'test path using str formatting: /home/sherms/{0}'.format(stamp)
testPath = 'test path using str formatting: /home/sherms/{:%d%m%y-%H:%M:%S}'.format(stamp)

print(path) # works
print(testPath)

# format timedate to: dd-mm-yy hh:mm:ss
# 240521: formatted timedate - refer to testPath var.
