#!/usr/bin/python3
def solution(a, n):
    count = 0
    if n < 1:
        return 0
    k = sorted(a)
    if k == a:
        return 1
    mylist = []
    for x, y in zip(a,k):
        if x - y != 0:
            mylist.append(x - y)
    if len(mylist) == 2:
        return 1
    return 0

a = [1,5,3,3,7]
print(solution(a,5))