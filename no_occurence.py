#!/usr/bin/python3
#note 11% 
def solution(A):
    l = len(A)
    a = sorted(A, reverse=True)
    for i in range(len(a) - 1):
        if a[i] < 0:
            return 1
        if a[i] - a[i+1] != 1:
            return a[i + 1] + 1
        else:
            if min(a) == 1:
                return max(a) + 1
            else:
                return min(a) - 1


A = [1, 3, 6, 4, 1, 2]
B = [2, 3, 4, 6]
c = [-1,-3]
D = [1,2,4]
print(solution(A))
print(solution(B))
print(solution(D))