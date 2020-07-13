#include<string.h>
#include<stdio.h>


int  main() {
char num[99], onedig[99],tens[99];

printf("Enter word to turn into integer: ");
fgets(num, sizeof(num), stdin);
strtok(num, "\n");
int num10=word2int(tens);
int num1=word2int(onedig);
int res;
res=num10+num1;
res=word2int(num);

printf("word as an int is %d. \n", res);
return 0; 
}

int word2int(char *word) {
char *ones[10]={"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
if(strcmp(ones[0], word)==0){
return 1;
}else if(strcmp(ones[1], word)==0){
return 2;
}else if(strcmp(ones[2], word)==0){
return 3;
}else if(strcmp(ones[3], word)==0){ 
return 4;
}else if(strcmp(ones[4], word)==0){
return 5;
}else if(strcmp(ones[5], word)==0){
return 6;
}else if(strcmp(ones[6], word)==0){
return 7;
}else if(strcmp(ones[7], word)==0){
return 8;
}else if(strcmp(ones[8], word)==0){
return 9;
}
char *next[10]={"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
if(strcmp(next[0], word)==0){
return 10;
}else if(strcmp(next[1], word)==0){
return 11;
}else if(strcmp(next[2], word)==0){
return 12;
}else if(strcmp(next[3], word)==0){
return 13;
}else if(strcmp(next[4], word)==0){
return 14;
}else if(strcmp(next[5], word)==0){
return 15;
}else if(strcmp(next[6], word)==0){
return 16;
}else if(strcmp(next[7], word)==0){
return 17;
}else if(strcmp(next[8], word)==0){
return 18;
}else if(strcmp(next[9], word)==0){
return 19;
}

char *tens[10]={"twenty", "thirty", "forty", "fifty", "fifty", "sixty", "seventy", "eighty", "ninety"};
if(strcmp(tens[0], word)==0){
return 20;
}else if(strcmp(tens[1], word)==0){
return 30;
}else if(strcmp(tens[2], word)==0){
return 40;
}else if(strcmp(tens[3], word)==0){
return 50;
}else if(strcmp(tens[4], word)==0){
return 60;
}else if(strcmp(tens[5], word)==0){
return 70;
}else if(strcmp(tens[6], word)==0){
return 80;
}else if(strcmp(tens[7], word)==0){
return 90;
}
}















