import binascii
x=raw_input("Enter a string: ")
print "String to binary:",
st2b=binascii.a2b_base64(x)
print(st2b)
print "Binary to string:",
print(binascii.b2a_base64(st2b))
