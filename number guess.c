#include<stdio.h>
#include<math.h>
void guess(int N)
{
    int n,guess,nog=0;
    n=rand()%N;
    printf("enter the guessed  number:",n);
    do{
       if(nog>9)
        {
            printf("\nyou loose\n");
            break;
        }
        scanf("%d",&guess);
        if(guess>n&&guess<N)
        {
            printf("too high\n");
            nog++;
        }
        else if (guess<n&&guess<N)
        {
            printf("too low\n");
            nog++;
        }
        else if(guess=n&&guess<N)
        {
            printf("you guess correct nof guesses: %d the number is : %d",nog,n);
            nog++;
        }
        else printf("enter in the range of 1-%d",N); 
    }while (guess!=n);

}
int main()
{
    int N;
    printf("enter the max  number u want in the range:");
    scanf("%d",&N);
    guess(N);
    return 0;
    
}
