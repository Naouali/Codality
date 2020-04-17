#!/usr/bin/python3
def solution(a,b):
    count = 0
    l = set(range(a, b + 1))
    sqr = set(range(1, b + 1))
    for i in sqr:
        if i**2 in l:
            count+=1
    return count



print(solution(-2,19))