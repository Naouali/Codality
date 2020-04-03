#!/usr/bin/python3
def solution(A):
    # write your code in Python 3.6
    
    my_dictionary = {}
    odd_element = -1
    
    # create dictionary
    for item in A:
        print(item, end="")
        my_dictionary[item] = 0 
    print(my_dictionary)
    # counting
    for item in A:
        my_dictionary[item] += 1
    print(my_dictionary)
    # find odd element
    for key in my_dictionary:
        if (my_dictionary[key] % 2 != 0):
            odd_element = key
    
    return odd_element
a = [9,3,9,3,9,7,9]
print(solution(a))
