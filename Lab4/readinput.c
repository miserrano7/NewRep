#include<stdio.h>

int main () {
char input[100];
printf("Enter input please: ");
scanf("%[^\n]s",input);
printf("Your input is: %s \n",input);
return 0;
}

