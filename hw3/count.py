import sys
chars={}
infile=(sys.argv[1])
finput=open(infile, "r")
with finput as f:
   for line in f:
      for ch in line:
         if ch in chars:
            chars[ch] += 1
         else:
            chars[ch] = 1
         for k in list(chars):
            if not k.isalpha():
               del chars[k]
maxkey=max(chars,key=chars.get)
x=ord(maxkey)         
num=x-97
key=num-4
print ("Max character ",maxkey, "Key is ", key) 
   
