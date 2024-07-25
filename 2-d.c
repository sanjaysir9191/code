#include<stdio.h>
int main()
{
   printf("hello word");
   int arr[2][2]={{1,2},{1,63}};
   int i,j;

for (i=0;i<6;i++)
   {
for (j=0;j<2;j++){

   //  arr[i][]=arr[i];

   printf("%d ",arr[i][j]);

   }
   }
return 0;
}