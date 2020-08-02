import os

filepath='/home/mserrano2/final/FINALpython/encrypted/'
path2='/home/mserrano2/final/FINALpython/decrypted/'

print("Files decrypted to 'decrypted' copies.")
for filen in os.listdir(filepath):
   filewrite=path2+filen
   target=open(filewrite,"wb")
   fileread=filepath+filen
   with open(fileread,"rb") as file1:
      byte=file1.read().decode('utf-8')
      key=150
      for bt in range(0, len(byte)):
         key=key-1
         if key<0:
            key=255
         num=ord(byte[bt])
         b=(chr((num-key-1)%256))
         target.write(b.encode('utf'))
   file1.close()
   target.close()
