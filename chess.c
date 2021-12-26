#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int marks_summation(int* marks, int number_of_students, char gender) {
  int as;
  if(gender=='g')
  {
      for(int i=0;i%2==0;i++)
      {
          as+=marks[i]+as;
          marks++;
      }
  }
  else {
      for(int i=0;i%2!=0;i++)
      {
          as+=marks[i]+as;
          marks++;
      }
  }
  return as;
}

int main() {
    int number_of_students;
    char gender;
    int sum;
  
    scanf("%d", &number_of_students);
    int *marks = (int *) malloc(number_of_students * sizeof (int));
 
    for (int student = 0; student < number_of_students; student++) {
        scanf("%d", (marks + student));
    }
    
    scanf(" %c", &gender);
    sum = marks_summation(marks, number_of_students, gender);
    printf("%d", sum);
    free(marks);
 
    return 0;
}
