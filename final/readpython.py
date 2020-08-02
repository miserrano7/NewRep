import os

filepath='/home/mserrano2/final/FINALpython/copies/'
path2='/home/mserrano2/final/FINALpython/encrypted/'

print("Files encrypted to 'encrypted' directories.")
for filen in os.listdir(filepath):
   filewrite=path2+filen
   target=open(filewrite,"wb")
   fileread=filepath+filen
   with open(fileread,"rb") as file1:
      byte=file1.read(1)
      key=150
      res=""
      while byte!=b'':
         key=key-1
         if key<0:
            key=255
         b=(chr((ord(byte)+key+1)%256))
         target.write(b.encode('utf-8'))
         byte=file1.read(1)
   file1.close()
   target.close()

















