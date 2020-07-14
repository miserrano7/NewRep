#include<stdio.h>
#include<stdlib.h>
int main(int argc, char *argv[]) {

int num;
char x;
char y;
int enk = atoi(argv[1]);
FILE *in = fopen (argv[2],"r");
FILE *out = fopen (argv[3],"w");
  
  
do { y=(char)x;
char let = y;;
  
if(let>='A'&& let<='Z')
let+=32;
  
if(let>='a' && let<='z'){

num=(let+enk-97)%26;
let = num +97;;
fprintf(out, "%c",let);
  
} else
fprintf(out, "%c",y);  
} while ((x=fgetc(in)) != EOF);
fclose(in);
fclose(out);

return 0;
}

