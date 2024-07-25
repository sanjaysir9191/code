from abc import ABC, abstractmethod
class A:
    @abstractmethod
    def function(self):
        print("this is 1")
    def function(self):
        print(" this is function 2")
class B(A):
    def  function(self):
        print("this is fuction3")
    # def function(self):
        pass    
        # print("b")
class C(B):
    print("this is c") 

a=A()
b=B()
c=C()
a.function()       
a.function()
b.function()
b.function()
c.function()