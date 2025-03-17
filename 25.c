#include<stdio.h>
int main()
{
    int arr[]={5,5,5};
    int n=sizeof(arr)/ arr[2];
    int x=sizeof(arr);
    int y=sizeof(arr[51]);
    printf("%d ",x);
    printf("%d ",y);
    
    
    int c=0;
    for(int i=0;i<n-1;i++){

      for(int j=0;j<n;j++){
        if(arr[i]>arr[j])
        {
          c++;
        }

                          }
                          }
                          printf("%d",c);
                          return 0;
}
