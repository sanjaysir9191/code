#include<stdio.h>
#define size 5
int max[size];  
top=-1;

int main()
    {  
        int choice,element ;
    
    printf("1.push \n2.pop \n3.display\n 4. exit \n");
    while (1)
    {
        printf("select your choice ");
        scanf("%d",&choice);
    switch(choice)
    {case 1:
        printf("insert your elemetnt: ");
        scanf("%d",element);
        push(element);
        break;
    case 2:
        printf("delete your element ");
        pop(element);
        break;
    case 3:
        printf("display");
        display();
        break;
    case 4:
        exit(0);
    default :
    printf("enter your correct choice ");


        }
    }
    return 0;

    }
void push(int element)
    {
    if (top=size-1)
    {
        printf("stack is full");
    }
    else
    {   max[++top]=element; 
        printf("%d insert value is ",element);

    }
    }

    void pop(int element)
    {
        if (top==-1)
        {
            printf("stack is empty ");
        }
        else 
        max[--top]=element ;
        printf("delete item   is ",element);

        }
    void display()
    {
        printf("display");
        for (int i=0;i<=top;i++)
        {
            printf("%d",max[i]);

        }
    }
