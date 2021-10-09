#include<stdio.h>
int main()
{
    char name[100];
    int a=3;
    printf("%d\n",a);
    printf("enter your name miss/mr:");
    fgets(name,sizeof(name),stdin);
    printf("you entered:%s",name);
   
    mains();
    return 0;
}
int mains()
{
    char str[50];
    printf("Enter string: ");
    fgets(str, sizeof(str), stdin);             
    displayString(str);     // Passing string to a function.    
    return 0;
}
void displayString(char str[])
{
    printf("String Output:");
    puts(str);
    
}
