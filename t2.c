#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
int main()
{
int a;
a=fork();
if (a>0)
 {
printf("parent process os sucessful\n");
}
else if (a==0)
 {
printf("child process is running \n");
}
else
printf(" PARENTS PRCESS IS UNSUCESSFUL\n");
return 0;
}
