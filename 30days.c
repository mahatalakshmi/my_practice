#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int n,t;
char a[50],out,out2;
scanf("%d",&t);
while(t--)
{
scanf("%s",a);
n=strlen(a);

for(int i=0;i<n;i++)
{
    if(i%2==0 || i==0)
    {
        printf("%c",a[i]);
        
    }
    
}
printf(" ");
for(int j=0;j<n;j++)
{
    if(j%2!=0 )
    {
        printf("%c",a[j]);
        
    }
    
}

}
}