#include<stdio.h>
extern int count;
void some()
{
    count=5;
    printf("%d",count);
}