import re

ones = ["zero", "one", "two", "three","four","five","six","seven","eight", "nine"] 
teens= ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["ten", "twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def word2int(str):
   try:
      inte=ones.index(str)
   except:
      try:
         inte=teens.index(str)+11
      except:
         inte=tens.index(str)+1
         inte=inte*10
   return inte;
  
   
word=input('Enter one word to change to int: ')
if re.search('-',word):
   word=word.split('-')
   res=word2int(word[0])
   newres=str(res)
   l=int(len(newres)/2)
   first,second=newres[:l], newres[l:]
   num=int(first)
   res1=word2int(word[1])
   s1=str(num)
   s2=str(res1)
   s=s1+s2
   final=int(s)
   print('word to int is:' , final)

else:
   word=word.split('-')
   res3=word2int(word[0])
   print('word to int is:', res3)
