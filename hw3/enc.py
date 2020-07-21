import sys

ikey=int(sys.argv[1])
infile=sys.argv[2]
finput=open(infile, "r")
outfile=sys.argv[3]
foutput=open(outfile,"w")

while 1:
   c=finput.read(1)
   if not c: 
      break
   if c.isalpha():
      c=c.lower() 
      num=((ord(c)-97)+ikey)%26
      c=chr(97+num)
      foutput.write(c) 
   else: 
      foutput.write(c)
finput.close()
foutput.close()

