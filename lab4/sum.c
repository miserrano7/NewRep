#include <stdio.h>

int main () {
int num;
int sum;

for (num=0;num <1000; num++) {
if ((num%3==0) || (num%5==0)){
sum+=num;
}
}
printf("The sum of the numbers is %d\n", sum);
return 0;
}
