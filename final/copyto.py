import shutil
import os.path 

#copying first file
file1= open("FINALinstruction","rb")  
file1.seek(-5,2) #xx2
data = file1.read(1)
txt=file1.readline().decode('utf-8')
txt=txt.strip('\n')
path1=os.path.join("/home/mserrano2",txt)
shutil.copy2(path1, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path1, "/home/mserrano2/final/FINALpython/copies")
file1.close()

#copying second file
file2= open("FINALinstruction","rb")
file2.seek(-97,2) #readme
data2 = file2.read(1)
txt2=file2.readline().decode('utf-8')
txt2=txt2.strip('\n')
path2=os.path.join("/home/mserrano2",txt2)
shutil.copy2(path2, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path2, "/home/mserrano2/final/FINALpython/copies")
file2.close()

#copying third file
file3= open("FINALinstruction","rb")
file3.seek(-186,2) #pusher
data3 = file3.read(1)
txt3=file3.readline().decode('utf-8')
txt3=txt3.strip('\n')
path3=os.path.join("/home/mserrano2",txt3)
shutil.copy2(path3, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path3, "/home/mserrano2/final/FINALpython/copies")
file3.close()

#copying fourth file
file4= open("FINALinstruction","rb")
file4.seek(-273,2) #path
data4 = file4.read(1)
txt4=file4.readline().decode('utf-8')
txt4=txt4.strip('\n')
path4=os.path.join("/home/mserrano2",txt4)
shutil.copy2(path4, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path4, "/home/mserrano2/final/FINALpython/copies")
file4.close()

#copying fifth file
file5= open("FINALinstruction","rb")
file5.seek(-370,2) #newper
data5 = file5.read(1)
txt5=file5.readline().decode('utf-8')
txt5=txt5.strip('\n')
path5=os.path.join("/home/mserrano2",txt5)
shutil.copy2(path5, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path5, "/home/mserrano2/final/FINALpython/copies")
file5.close()


#copying sixth file
file6= open("FINALinstruction","rb")
file6.seek(-463,2) #hello
data6 = file6.read(1)
txt6=file6.readline().decode('utf-8')
txt6=txt6.strip('\n')
path6=os.path.join("/home/mserrano2",txt6)
shutil.copy2(path6, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path6, "/home/mserrano2/final/FINALpython/copies")
file6.close()

#copying seventh file
file7= open("FINALinstruction","rb")
file7.seek(-553,2) #message
data7 = file7.read(1)
txt7=file7.readline().decode('utf-8')
txt7=txt7.strip('\n')
path7=os.path.join("/home/mserrano2",txt7)
shutil.copy2(path7, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path7, "/home/mserrano2/final/FINALpython/copies")
file7.close()


#copying eighth file
file8= open("FINALinstruction","rb")
file8.seek(-647,2) #tar
data8 = file8.read(1)
txt8=file8.readline().decode('utf-8')
txt8=txt8.strip('\n')
path8=os.path.join("/home/mserrano2",txt8)
shutil.copy2(path8, "/home/mserrano2/final/FINALc/copies")
shutil.copy2(path8, "/home/mserrano2/final/FINALpython/copies")
file8.close()

print("Files have been copied to copies in FINALc and FINALpython.")
