from array import *
import numpy
"""arr1=array([1,2,3,4])
arr2=arr1.copy()#copy means deap copy so not change the arr1 means previes value and copy value output is previes value 
arr1[2]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))"""
#write a code add two arrays using for loop?
arr=array("i",[1,2,3,4])
arr1=array("i",[5,6,7,8])
for i in arr1:
    arr.append(i)
print(arr)
#write a code find a maximum value with out using a built in applicaton?
def maximum_array_(arr):
    maxi=arr[0]
    for i in arr:
        if i > maxi:
            maxi=i
    return maxi
print("maximum value in array:",maximum_array_([67,89,90,234,678]))




