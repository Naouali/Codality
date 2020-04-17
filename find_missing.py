#!/usr/bin/python3
#find the missing element 
#note 20% time to accomplish 10mincl --> without using sets
#second note 50% with sets 20% correctness and 80% performance
# def solution(A):
#     a = sorted(A)
#     a = set(a)
#     mini = min(a)
#     maxi = max(a)
#     my_list = sorted(list(range(mini, maxi + 1)))
#     for i in set(my_list):
#         if i not in a:
#             return i


#second algo 50% --->20% correctness 80% performance
def solution(A):
    if len(A) == 1:
        return A[0]
    a = sorted(A, reverse=True)
    for i in range(len(a) - 1):
        if a[i] - a[i + 1] != 1:
            return a[i+1] +1



a = [1,3,5]
print(solution(a))