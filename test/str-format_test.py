import datetime

stamp = datetime.datetime.now()
path = 'test path using str formatting: /home/sherms/{0}'.format(stamp)

print(path) # works

# format timedate to: dd-mm-yy hh:mm:ss
