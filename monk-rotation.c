#include<stdio.h>
int main()
{
    int a,b,t,i,j,k,m[a],h;
    printf("enter no of test cases:");
    scanf("%d",&t);
    for ( i = 0; i < t; i++)
    {
        printf("length of the array:");
        scanf("%d",&a);
        printf("no of rotations:");
        scanf("%d",&b);
        printf("enter elements:");
        for ( k = 0; k < a; k++)
        {
            scanf("%d ",&m[k]);
        }
         for (i=0;i<b;i++)
         {
           int last;
           last=m[k-1];
           for( j = k-1; j >0; j++)
           {
               m[j]=m[j-1];
           }
           m[0]=last;
         }
         for ( h = 0; h < a; h++)
         {
           printf("the arry after rottion:%d",m[h ]);
         }
         
         
        
    }
    
}
