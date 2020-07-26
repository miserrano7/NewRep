import binascii
def dhex(hfile):
    d=open(hfile,"r").read()
    dhex=binascii.unhexlify(d)
    print "The dehexed text is:\n",
    print (dhex)
dhex("hexd")
