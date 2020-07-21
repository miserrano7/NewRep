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

word=input('Enter two nums in word form to multiply: ')
if re.search('-',word):
   newword=word.replace(" ", "-")
   newword=newword.split('-')
   res=word2int(newword[0])
   newres=str(res)
   l=int(len(newres)/2)
   first,second=newres[:l], newres[l:]
   num=int(first)
   res1=word2int(newword[1])
   s1=str(num)
   s2=str(res1)
   s=s1+s2
   final=int(s)


   res2=word2int(newword[2])
   newres2=str(res2)
   l=int(len(newres2)/2)
   first2,second2=newres2[:l], newres2[l:]
   num2=int(first2)
   res3=word2int(newword[3])
   s3=str(num2)
   s4=str(res3)
   snxt=s3+s4
   finalnext=int(snxt)
   #print('word to int is:' , final)
   print("Product is:", final*finalnext )

else:
   word=word.split(' ')
   res5=word2int(word[0])
   res6=word2int(word[1])
  #print('word to int is:', res3)
   print("Product is:", res5*res6)

