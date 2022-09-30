# programmers, phase1 : 행렬의 덧셈, python3
def solution(A, B):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] += B[i][j]
    return A
