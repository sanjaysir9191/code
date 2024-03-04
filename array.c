#include<stdio.h>
int main()
    { 
    int size,i;
    int max=0;
    
    printf("enter your size:");
    scanf("%d",&size);
    int array[size];
for (int i=0;i<size;i++)
    {
    printf("print the size of the array %d:",i+1);
    scanf("%d",&array[i]);
    }

for(i=0;i<size ;i++)
    {
    if (array[i]>max)
        {
            if(array[i-1]<array[i]&& array[i+1]<array[i]){
                max=array[i];
            }
        
        }

    }
printf("%d",max);


return 0;
}