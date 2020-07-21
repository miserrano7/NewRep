max1=0
for num1 in range(100,1000):
   for num2 in range(100,1000):
      mult=num1*num2
      rev=0
      comp=mult
      while comp!=0: 
         rev=(10*rev)+(comp%10)
         comp/=10
         if((mult>max1) and (mult==rev)): 
            max1=mult
print"the largest palindrome is",
print (max1) 
