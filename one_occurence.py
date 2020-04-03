#!/usr/bin/python3
"""find the number that occure only one time in an array"""
def solution(A):
    for i in A:
        if A.count(i) == 1:
            return i
