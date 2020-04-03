#!/usr/bin/python3
"""find the number that occure only one time in an array"""
def solution(A):
    for i in A:
        if A.count(i) == 1:
            return i
#This algorithm is correct by it will take O(n²) to pass, which is not so optimal
#another solution is:

def solution(A):
    for i in range(len(A)):
        A.sort()

        if A[i] > A[i - 1] and A[i] < A[i + 1]:
            return A[i]
#also not very optimal the built in python method sort() takes n log n time complexity, which is horrible
def solution(A):
    A = sort_it(A)
    for i in range(len(A) - 1):
        if A[i] > A[i - 1] and A[i] < A[i + 1]:
            return A[i]
   
#also this algorithms is correct but it takes to much time o(n2)

def sort_it(arr):
    n = len(arr)

    # Traverse through all array elements                               
    for i in range(n):

        # Last i elements are already in place                          
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1                        
            # Swap if the element found is greater                      
            # than the next element                                     
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
### The perfect answer is:
def solution(A):
    result = 0   
    for number in A:     
        result ^= number   
    return result

###another good answer is :
def solution(A):
    dic = {}
    value = 0
    for i in A:
        dic[i] = 0
    for i in A:
        dic[i] += 1
    for j in dic:
        if dic[j] == 1:
            value = j
    return j
