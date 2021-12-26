#include<stdio.h>  
int main(){    
int n,i,t,m=0,j,flag=0; 
printf("enter test cases:");scanf("%d",&t);  
for(j=0;j<t;j++)
{ 
printf("Enter the number to check prime:");    
scanf("%d",&n);    
m=n/2;    
for(i=2;i<=m;i++)    
{    
if(n%i==0)    
{    
printf("Number is not prime");    
flag=1;    
break;    
}    
}    
if(flag==0)    
printf("Number is prime");     

}
 }    