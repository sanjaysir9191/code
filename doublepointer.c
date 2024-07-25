#include<stdio.h>
int main()
{

    int a=20;
   int  *ptr1;
   int **ptr2;
    
    ptr1=&a;
    ptr2=&ptr1;
    
    printf("value of a %d:\n ",a);
    printf("1st pointer %d :\n ",*ptr1);
    printf("value of 2nd pointer %d:\n ",**ptr2);


    return 0;


}