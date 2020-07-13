#include<stdio.h>
#include<ctype.h>
#include<string.h>


char input[2];
int main () {

        printf(" Enter the integer number: ");
        
        scanf("%s",&input);
        char one = input[0];
        char two = input[1];


                        

if (input[0]!= '\0' && input[1]=='\0'){                      //to print 0=9
if(one=='0') 
printf("zero\n");
if(one=='1') 
printf("one\n");
if(one=='2') 
printf("two\n");         
if(one=='3') 
 printf("three\n");
if(one=='4') 
printf("four\n");         
 if(one=='5') 
 printf("five\n");
if(one=='6') 
printf("six\n");
if(one=='7') 
printf("seven\n");
if(one=='8') 
printf("eight\n");
if(one=='9') 
printf("nine\n");               
} 
else { 

 
// to print 10-19                    

 if(one=='1') {                               
 if(two=='0') {
 printf("Ten\n");
}
 if(two=='1')  {
 printf("Eleven\n");
}
 if(two=='2') {
 printf("Twelve\n");
} 
 if(two=='3') {
 printf("Thirteen\n");
}
 if(two=='4'){
 printf("Fourteen\n");
}
if(two=='5'){
printf("Fifteen\n");
}
if(two=='6'){
printf("Sixteen\n");
}
if(two=='7') {
printf("Seventeen\n");
}
if(two=='8') {
 printf("Eighteen\n");
}
 if(two=='9') {
printf("Nineteen\n");
  }       
} 




 if(one=='2') {
  if  (two=='0') 
 printf("Twenty\n");
  else{ 
 printf("Twenty-"); 
 printf("\n", onedigit());
 }
}

                                       
  if(one=='3') {
   if ( two=='0')
   printf("Thirty\n");
    else {
   printf("Thirty-"); 
   printf("\n", onedigit());
  }
}

                                        
                        
  if(one=='4'){
  if(two=='0')
   printf("Fourty\n");
  else {
  printf("Fourty-"); 
  printf("\n", onedigit());
   }
  }
  
  if(one=='5') {
  if(two=='0')
  printf("Fifty\n");
  else {
  printf("Fifty-"); 
   printf("\n", onedigit());
   }                                       
  }
  
  if(one=='6') {
  if(two=='0')
  printf("Sixty\n");
  else {
  printf("Sixty-"); 
  printf("\n", onedigit());
   }                                       
  }
                       
  if(one=='7') {
  if(two=='0')                                       
 printf("Seventy\n");                                
else {                                       
 printf("Seventy-");                                         
printf("\n", onedigit());
 }
}
 
 if(one=='8') {
 if(two=='0')
 printf("Eighty\n");
 else {
 printf("Eighty-");
 printf("\n", onedigit());
  }  
} 

 if(one=='9') {
  if(two=='0')
 printf("Ninety\n");
 else {
 printf("Ninety-");
 printf("\n", onedigit());
    }                                       
  }
}
                       
 return 0;     
}



int onedigit() {
char firstdigit[10][10]={"zero", "one", "two",
                               "three", "four","five",
                          "six", "seven", "eight", "nine"};


if(input[1]=='0') {
printf("%s", firstdigit[0]);
}
if(input[1]=='1'){
printf("%s",firstdigit[1]);
}
if (input[1]=='2') {
printf("%s", firstdigit[2]);
}
if(input[1]=='3') {
printf("%s", firstdigit[3]);
}
if(input[1]=='4'){
printf("%s", firstdigit[4]);
}
if(input[1]=='5') {
printf("%s", firstdigit[5]);
} 
if(input[1]=='6') {
printf("%s", firstdigit[6]);
}
if(input[1]=='7') {
printf("%s", firstdigit[7]);
}
if(input[1]=='8') {
printf("%s", firstdigit[8]);
}
if(input[1]=='9') {
printf("%s", firstdigit[9]);
}
}
