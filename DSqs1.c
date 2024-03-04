// Name : SANJAY GUPTA Course & Sec : MCA ‘c’ Roll No : 74
// Q. Write a menu-driven program for following operations on stack for using array(call by
// reference).
// Operations : Push,Pop,Display,Peek,Exit.
// Code:
#include<stdio.h>
#include<stdlib.h>
#define max 10
int push(int [],int*);
int pop(int [],int*);
void display(int[],int);
void peek(int [],int);
int main(){
int stack[max],top=-1,ch;
char choice;
do{
printf("\n1. Push \n2. Pop \n3. Display\n4. Peek \n5. Exit \n");
printf("\nEnter your choice : ");
scanf("%d",&ch);
switch(ch){
case 1:
top=push(stack,&top);
break;
case 2:
top=pop(stack,&top);
break;
case 3:
display(stack,top);
break;
case 4:
peek(stack,top);
break;
case 5:
printf("\nDo you want to continue your program? (Y/N) : ");
scanf(" %c",&choice);
if(choice == 'N' || choice == 'n'){
exit(0);
}
break;
default:
printf("Invalid Choice..\n");
}
}while(ch<=5);
return 0;
}
int push(int stack[], int *top){
int n;
if(*top==max-1){
printf("Stack Is Overflow..");
}else{
printf("\nEnter value : ");
scanf("%d",&n);
(*top)++;
stack[*top]=n;
}
return *top;
}
int pop(int stack[], int *top){
int n;
if(*top==-1){
printf("Stack is Underflow..");
}else{
(*top)--;
printf("\nElement Popped..\n");
}
return *top;
}
void display(int stack[], int top){
int temp=top;
if(temp==-1){
printf("Stack is Empty..");
}else{
while(temp>=0){
printf("Element is : %d \n",stack[temp]);
temp--;
}
}
}
void peek(int stack[],int top){
if(top==-1){
printf("Stack is Empty..");
}else{
printf("\nPeek Element is : %d \n",stack[top]);
}
}

