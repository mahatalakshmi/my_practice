#include <stdio.h>
 
int tower(int n,char from,char to,char aux)
{
    if(n==1)
    {
        printf("move disc 1 from %c to peg %c\n",from,to);
        return ;
    }
    tower(n-1,from,aux,to);
    printf("move disc %d form %c to %c\n",n,from,to);
     tower (n-1,aux,to,from);
}
int main()
{
    int n=4;
    tower(n,'a','b','c');
    return 0;
}
