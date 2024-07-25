#include<stdio.h>
#include<stdlib.h>
typedef struct node{
int info;
struct node *next;
}nd;
void push(nd**);
void pop(nd**);
void display(nd*);
int main(){
int *top=NULL;
int choice;
do{
printf("\n1. Push \n2. Pop \n3. Display \n4. Exit \n");
printf("Enter The choice : ");
scanf("%d",&choice);
switch(choice){
case 1:
push(&top);
break;
case 2:
pop(&top);
break;
case 3:
display(top);
break;
case 4:
exit(0);
default:
printf("Invalid Choice.. ");
}
}while(choice<=4);
return 0;
}
void push(nd** tp){
nd *p;
p=(nd*)malloc(sizeof(nd*));
if(p==NULL){
printf("\n Stack is not enough memory..");
}else{
int num;
printf("\nEnter the element : ");
scanf("%d",&num);
p->info=num;
p->next=*tp;
*tp=p;
}
}
void pop(nd** tp){
nd *temp;
if(*tp==NULL){
printf("\nStack is Underflow..");
}else{
temp=*tp;
printf("\nPopped element is : %d \n",(*tp)->info);
*tp=(*tp)->next;
free(temp);
}
}
void display(nd* top){
if(top==NULL){
printf("\n Stack is empty..");
}else{
nd *temp;
temp=top;
while(temp!=NULL){
printf("Element : %d \n",temp->info);
temp=temp->next;
}
}
}