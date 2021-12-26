#include<stdio.h>
int main()
{
    int n,m;
    printf("enter no of students:");
    scanf("%d",&n);
    m=n*((n-1)/2);
    printf("total no of handshakes is=%d",m);
}