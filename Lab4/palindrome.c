#include <stdio.h>


int main (){
int mult;
int max=0;
int i;
int j;

for(i=100; i <=999; i++) {
for (j=100; j<=999; j++){
mult=i*j;
int rev=0;
int comp;
comp=mult;
while (comp !=0){
rev=(10*rev)+(comp%10);
comp/=10;
}
if((mult>max && mult==rev)){
max=mult;
}
}
}
printf("Largest pal is %d \n", max);
return 0;
}





















//int pal(int x) {
//int rev=0;
//int back; 
//back=x;
//while(x!=0) {
//rev=(10*rev)+(x%10);
//x/=10;
//x=rev;
//}
//if(back==rev) {
//printf("this is pal");
//return (rev);
//}
//}



