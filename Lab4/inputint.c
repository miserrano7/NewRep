#include<stdio.h>

int main() {

char num[100];
printf("Enter a number: ");
scanf("%s", num);
int num2;
num2=atoi(num);
printf("The number is %d in integer form\n", num2);
return 0;
}
