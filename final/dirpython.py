import os
import shutil

path="FINALpython"
path2="FINALpython/copies"
path3="FINALpython/encrypted"
path4="FINALpython/decrypted"

try: 
   os.mkdir(path)
   os.mkdir(path2)
   os.mkdir(path3)
   os.mkdir(path4)
except OSError: 
   print("Cannot make directory and subdirectories.")
else:
   print("Directories created.")

shutil.copy2("/home/mserrano2/final/dirpython.py", "/home/mserrano2/final/FINALpython/")
