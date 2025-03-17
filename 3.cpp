#include<iostream>
using namespace std;
int main()
{
// int i,y;
// y=30;
// char n= 'a';
// this is first
// for(i=0;i<y;i++)
// {
// cout<<(char)(n+i);
// }


// this is second

// int i,j,n;
// n=5;
// char a='a';
// for (i=0;i<n;i++)
// {    
//     for(j=0;j<i;j++)
//     {
//         cout<<" ";
//     }
//     for(j=0;j<n-i;j++)
//     {
//             cout<<(char)(a+i);
//     }
// cout<<endl;
// }

// this is third 


int i,j,n;
n=5;
int x=1;
// char a='a';
for (i=0;i<n;i++)
{    
    for(j=0;j<i-1 ;j++)
    {
        cout<<"*";
    }
    for(j=0;j<n;j++)
    {
            cout<<x;
             x++;
    }
cout<<endl;
}


return 0;



}