# https://stackoverflow.com/questions/35424831/python-how-to-copy-content-of-usbflash-to-system-directory
# below code is from above link.
# how to copy a file to a USB.
# from last response - bottome of page.

'''
import os
file = "cat.jpg"
os.system("for /F \"tokens=1*\" %a in (\'fsutil fsinfo drives\') do (for %c in (%b) do (for /F \"tokens=3\" %d in (\'fsutil fsinfo drivetype %c\') do (if %d equ Removable (copy " + file + " %c))))")
'''

