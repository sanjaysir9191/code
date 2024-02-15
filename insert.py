# create a list 
x=[2,4,6,3,1,5]
i=0
if x[0] < x[1]:
    x[0]==x[1]


    print(x[0])
   ##insertion short?
   # -*- coding: utf-8 -*- 

unsorted_list = [20, 7, 3, 4, 12, 2, 1]

#Insertion Sort

#Pseudocode

# for i ← 1 to length(A)
#     x ← A[i]
#     j ← i
#     while j > 0 and A[j-1] > x
#         A[j] ← A[j-1]
#         j ← j - 1
#     A[j] ← x

def insertion_sort(a):
	for i in range(1, len(a)): #starts with second element
		x=a[i] #the element to be compared with the elements in sorted list
		j=i #index of the element
		while j>0 and a[j-1] > x: #compares and updates the element starting from the biggest element in the sorted list 
			a[j]=a[j-1] #if the next biggest element in the sorted list is bigger than our element,
						#we move this biggest element to our element's position 
			j=j-1 #decrease it to make the same comparison until the first element or no update occurs
		a[j]=x #finally add our element to the last updated element's position.
	print("after insertion sort:")
	print(a)

insertion_sort(unsorted_list)