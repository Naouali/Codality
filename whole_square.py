#!/usr/bin/python3
def solution(A):
    def solution(a,b):
    count = 0
    l = set(range(a, b + 1))
    sqr = set(range(1, b + 1))
    for i in sqr:
        if i**2 in l:
            count+=1
    return count

a =  [7, 2, 3, 6, 5, 9, 1, 4, 8]
c = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(solution(a))
print(solution(c))