#usr/bin/python3
def solution(N):
    """codality bits gap challenge"""
    binary = bin(N) #turn N into binary
    ones = 0
    zeros = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            ones += 1
        if binary[i] == "0":
            zeros += 1
    if zeros <= 1: #if ther is no "1" or only one "1" return 0
        return 0
    elif ones <= 1: #if there is no "0" or only one "0" return 0
        return 0
    else:
        binary = binary[2:] #eliminate 0b caracter
        m = binary.split("1") #split the string based on "1" occurence
        l = max(m) #retrive the max chuck of zero
        return len(l) #return it's length
