import numpy as np 


x=[0,1,2,3,4,5,6,7,8,9]
y=np.array(x)
print(type(x))
print(type(y))
# print(x,y)

l=[]
for  type1 in range(1,5):
    # type1=int(input("enter number :"))
    l.append(type1)
a=np.array(l)
print(type(a))
print(a)    
print(a.ndim)
x=np.array([25])
print(x)
print(x.ndim)
# print(x.dim)
# ################zeroes elements################
# zero_array=np.zeros(0) 
# zero_array=np.zeros(())
# zero_array=np.zeros() 
zero_array=np.zeros((()))
print(zero_array)
print(type(zero_array))

one_array=np.ones((8))
print(one_array)
print(type(one_array))

s=np.arange(9)
print(s)
print(type(s))
arr_empty=np.empty((0))
print(arr_empty)
# //////print a diognaal array
a=np.eye(3,7)
print(a)
# linespace 
arr_gap=np.linspace(0,5,30)
print(arr_gap)
#  raandom  in numpy 
rand_array=np.random.rand(5)
print(rand_array)
randn_array=np.random.randn(2)
print(randn_array)
ranf_array=np.random.ranf(8)
print(ranf_array)
randint_array=np.random.randint(4,6,8)
print("data type ",randint_array.dtype)
print(randint_array)
f=np.array([1,2,3,4],dtype=np.int8)
print("datatype:",f.dtype)
new=np.float32(f)
print(new.dtype)
