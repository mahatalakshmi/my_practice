#include<stdio.h>
#include<time.h>
int rps(char you,char comp)
{
    if(you==comp)
    {
        return 0;
    }
    if((you=='r'&&comp=='p') ||(you=='s'&&comp=='r')||(you=='p'&&comp=='s') )
    {
        return -1;
    }
    if((you=='p'&&comp=='r')||(you=='r'&&comp=='s')||(you=='s'&&comp=='p'))
    {
        return 1;
    }
}
int main()
{
    char you,comp,i=0;
    printf("type the choice you made(r for rock;s for scissors;p for paper):");
    
    
    srand(time(0));
    int number=rand()%100;
    if (number<=33)
    {
        comp='r';
    }
    else if(number>33&&number<=66)
    {
        comp='p';
    }
    else if(number>66)
    {
        comp='s';
    }
    scanf("%c",&you);
    printf("you ");

    int result=rps(you,comp);
    if(result==0)
    {
        printf("draw");
    }
    if(result==1){
        printf("won");

    }
    else if (result==-1){printf("lost");}
    printf(" you choose %c and computer choose %c\n" ,you ,comp);
    
    
    printf("\t\tgame over");
}

