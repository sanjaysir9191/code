#include<stdio.h>
#define size 100

int linearserach(int [],int);


int main()
{
int arr[size];
int i,n,f=0;
printf("enter the size of array:");
scanf("%d",&n);
for (i=0;i<n;i++)
{
    printf("enter the element %d:=",i+1);
    scanf("%d",&arr[i]);

}
f=linearserach(arr,n);

if (f==0)
{
    printf("\n element is not found");
}
else
printf("element is found ");



return 0;
}
linearserach(int arr[],int n)
{
    int key;
    printf("enter you want to serach ");
    scanf("%d",&key);
    for (int i=0;i<n;i++)
    {
        if (arr[i]==key)
         return i;

    }
  return 0;}