#include<stdio.h>

typedef struct band_details
{
    char band_name[50];
    char member_name[50];
    int no_of_members;
}band;
int main()
{
    struct band_details a1[25] ;
    struct band_details n1;
   
    
    int i;
    printf("Enter band name :");
    scanf("%s",n1.band_name);
    printf("enter no of members:");
    scanf("%d",&n1.no_of_members);
    for(i=0;i<=n1.no_of_members;i++)
    {
            
             fgets(a1[i].member_name,sizeof(a1[i].member_name),stdin);
              printf("\nenter name of the member:");
    }
    printf("\nband details:\n \t band name :%s \n\t\t\t no of member:%d \n", n1.band_name,n1.no_of_members);
    for  (i = 1; i <= n1.no_of_members; i++)
    {
        printf("\n\n\t\t\t name of members:");
        puts(a1[i].member_name);
    }
    


  return 0;

}
