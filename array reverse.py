
arr =([1,2,3,4,5])
# print(arr)
arr1=[0]*5
arr1[0]= arr[4]
arr1[1]=arr[3]
arr1[2]=arr[2]
arr1[3]=arr[1]
arr1[4]=arr[0]
# print(arr1)
cars = [1,2,3]
# print(cars)
print(arr[::-1])
arr.reverse()
print(arr)
a=list(reversed(arr))
print(a)

#The original array
arr = [12, 34, 56, 78]
print("Original Array is :",arr)
#reversing using reversed()
result=list(reversed(arr))
print(result)
print("Resultant new reversed Array:",result)



