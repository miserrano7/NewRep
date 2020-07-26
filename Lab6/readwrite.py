from os import system

path= '/home/mserrano2/Lab6/test'
bdata=open(path,"rb").read()
path2='/home/mserrano2/Lab6/testcopy'
newfile=open(path2, "wb")
newfile.write(bdata)
newfile.close()
system("chmod u+x testcopy")
system("./testcopy")
