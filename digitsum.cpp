#include<iostream>
using namespace std;

int sum1()
{ int sum,number,rem;
    cout<<"enter number=";
    cin>>number;
    sum=0;
    while(number>0)
    {rem=number%10;
        number=number/10;
        sum+=rem;
    }
return sum;
  cout<< sum;
}
int main()
{
// sum1();
    cout<<sum1();
// int number,i,sum;
// sum=0;
// cout<<"Enter a number: ";
// cin>>number;
// for(i=1;i<=number;i++)
// {  sum+=i;
// }
// cout<<"sum ="<<sum;

return 0;

}