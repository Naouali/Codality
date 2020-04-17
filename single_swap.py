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
        mylist.append(x - y)
    for i in mylist:
        if i != 0:
            count += 1
    if count == 2:
        return 1
    return 0



a = [1,5,3,3,7]
b = [1,3,5,3,4]
c = [1,3,5]
print(solution(c,5))