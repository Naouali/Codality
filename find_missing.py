#!/usr/bin/python3
#find the missing element 
#note 20% time to accomplish 10mincl
def solution(A):
    a = sorted(A)
    mini = min(a)
    maxi = max(a)
    my_list = sorted(list(range(mini, maxi + 1)))
    for i in my_list:
        if i not in a:
            return i





a = [1,2,4,5]
print(solution(a))