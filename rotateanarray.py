def solution(A, K):
    new = [0] * len(A)
    for i in range(len(A)):
        index = (i + K) % len(A)
        new[index] = A[i]
    return new
    
