#!/usr/bin/python3
#find the missing element 
#note 20% time to accomplish 10mincl --> without using sets
#second note 50% with sets
def solution(A):
    a = sorted(A)
    a = set(a)
    mini = min(a)
    maxi = max(a)
    my_list = sorted(list(range(mini, maxi + 1)))
    for i in set(my_list):
        if i not in a:
            return i





a = [1,2,4,5]
print(solution(a))