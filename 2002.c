#include<stdio.h>
int main()
{int x;
printf("enter size: ");
scanf("%d",&x);
int n[x];
for(int i=0;i<x;i++)
    {
    scanf("%d",&n[i]);
    }
for(int i=0;i<x;i++)
    {
    printf("%d \n",n[i]);
    }

    return 0;
}