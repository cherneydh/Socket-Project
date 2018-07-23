#solution for a user calling 'ls'
#calls ls -l in current directory
#will need to print this to the user
#must use python 3.7 for capture_output parameter
#other possible solution is os.scandir()
#https://docs.python.org/3/library/os.html#os.scandir

import subprocess

command = subprocess.run(["ls", "-l", "./"],capture_output=True,universal_newlines=True)
print (command.stdout)
