#include<stdlib.h>
#include<dirent.h>
#include<stdio.h>

#define path1 "/home/mserrano2/final/FINALc/copies/"
#define pathend "/home/mserrano2/final/FINALc/encrypted/"


int enc(file) {

fseek(path1,0,SEEK_END);
fl=ftell(path1);
fseek(path1,0, SEEK_SET);
int key = 150;
while(path1!=NULL){ 
//c + key
key = key - 1 > 0 ? ( key - 1 ) % 256 : 255;
}
}
int main() {

struct dirent *direc;
DIR*d=opendir(path1);

if (d==NULL) {
printf("Unable to open.");

} while((direc==readdir(d))!=NULL) {

char*s=direc->d_name;
if(strcmp(s,".")!=0 && strcmp(s,"..")) {
enc(s)
}
}
return 0;
}
