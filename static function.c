#include<stdio.h>
void fun();
static int count=5;
int main()
{
    while(count--)
    {
        fun();
    }
}
void fun()
{
    static int i=7;
    i++;
    printf("i=%d,count=%d \n",i,count);
}


