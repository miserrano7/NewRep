#include<stdio.h>
#include<stdlib.h>

int main(int argc, char*argv[]) {
  int chars[26]={0};
  

  FILE *fp = fopen(argv[1], "r");
  char c;
  int k;
  int max=0;
  int lnum;
 
  
  while((c=fgetc(fp)) !=EOF) {
   
      char ch=(char)c;
  
  if(ch>='A' && ch <='Z')
   ch+=32;
   
   if(ch>='a' && ch <='z') {
  int x=(ch-97)%26;
   lnum=(int)(x);
    chars[lnum]++;
    
}
} 
for(k=0; k<=26; k++) {
if(chars[k] > chars[max]) {
max= k;
}
}

int key=(max-4);
printf("max character is %c and key used was %d\n" , (char)(max+97),key); 
fclose(fp);
return key; 
}

