
import sys
import binascii
def fhexdump(rfile,wfile):
   hexst="";b=""
   with open(rfile, "rb") as hfile:
      b=hfile.read(2)
      x=""
      while b !=x:
         char2hex=binascii.hexlify(b)
         hexst += char2hex
         b=hfile.read(1)
   print "Text to hex is:",
   print hexst
   hfile=open(wfile, "w")
   hfile.write(hexst)
   hfile.close()
path=sys.argv[1]
fhexdump(path, "hexd") 


