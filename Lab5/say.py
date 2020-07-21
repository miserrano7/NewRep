import math
def int2words(n):
   inp=n.split(' ')
   inte=inp[0] 
   digits=len(inte)
   x=0
 
   ones = ["zero", "one", "two", "three","four","five","six","seven","eight", "nine"]
   middle = ["", "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
   tens = ["", "", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
   if (digits==1):
      ran=ones[ord(inte[0])-48]
      print(ran)
      return;
   while (x < digits):
      if (digits >= 3):
         if (ord(inte[0])-48 != 0):
           print(ones[ord(inte[x])-48])
         digits=digits-1
      else:
          if (ord(inte[x])-48 == 1):
             print(middle[(ord(inte[x])-48 + ord(inte[x])-48)])
             return;
          else:
             i = ord(inte[x])-48
             if(i > 0):
                print (tens[i],end = "-")
             #x=x+1
             x=x+1
             if(ord(inte[0])-48 != 0):
                print(ones[ord(inte[x])-48])
      x=x+1
res= int(input("Enter a number in integer form: "))
int2words(str(res));
