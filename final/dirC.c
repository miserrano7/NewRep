#include <stdio.h>
#include<sys/stat.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {
    if (mkdir("FINALc",0750) == -1) {
        
        mkdir("FINALc/copies", 0750);
        mkdir("FINALc/encrypted",0750);
        mkdir("FINALc/decrypted",0750);
         perror(argv[0]);
         exit(EXIT_FAILURE);
   }   
        FILE *fin=fopen("dirC.c","rb");
        FILE *fout=fopen("FINALc/copydirC.c", "wb");
      
        char ch;
        while (!feof(fin)) {
        fscanf(fin,"%c", &ch);
        fprintf(fout, "%c", ch);
      } 
   
      char c[600];
      system("gcc FINALc/copydirC.c -o copydirC.c");
      FILE *inp=fopen("FINALc/copyC.c", "r");
      FILE *outp=fopen(argv[1],"w");
      sprintf(c,"./FINALc/copydirC.c >>",outp); 
   return 0;
}

