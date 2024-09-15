# Checking if a file exists

import os

if os.path.isfile("file.txt"):
    print("File exists!")
else:
    print("File does not exists!")