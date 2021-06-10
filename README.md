# Quick-backup
- Python script to quickly backup data.
- copies selected folders to a target drive.

# Docs
Info about script:
- qb(5).py is the latest working version.
- it copies selected folders locally.
- copy function does not work in vs code. the following error is produced:
  - bash: syntax error near - unexpected token `(' - seems to be shutil.ignore_patterns('patterns').
- it works in vs code if you copy a sub directory of /home/sherms. ie: /home/sherms/resources.
- update file paths and folders to ignore in the copy function as required.
- cannot copy folder to another drive if it has a ':' in it. used '-' in the filename instead.
- list in the exlcuded function is inputted manually.

# Status
Active

# Timeline
- Started: Dec 2019 
- Finished: TBC
